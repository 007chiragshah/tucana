package org.sibel.mdib.overrides;

import com.google.inject.assistedinject.Assisted;
import com.google.inject.assistedinject.AssistedInject;
import com.google.inject.name.Named;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.security.cert.X509Certificate;
import java.util.Collections;
import java.util.List;
import java.util.Optional;
import java.util.function.Supplier;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.eclipse.jetty.http.HttpHeader;
import org.eclipse.jetty.http.HttpStatus;
import org.eclipse.jetty.io.Content;
import org.eclipse.jetty.server.Handler;
import org.eclipse.jetty.server.Request;
import org.eclipse.jetty.server.Response;
import org.eclipse.jetty.util.Callback;
import org.eclipse.jetty.util.ssl.X509;
import org.somda.sdc.common.CommonConfig;
import org.somda.sdc.common.logging.InstanceLogger;
import org.somda.sdc.dpws.CommunicationLog;
import org.somda.sdc.dpws.DpwsConfig;
import org.somda.sdc.dpws.http.HttpException;
import org.somda.sdc.dpws.http.HttpHandler;
import org.somda.sdc.dpws.soap.CommunicationContext;
import org.somda.sdc.dpws.soap.HttpApplicationInfo;
import org.somda.sdc.dpws.soap.TransportInfo;

/**
 * {@linkplain Handler.Abstract} implementation based on Jetty HTTP servers.
 */
public class CustomJettyHttpServerHandler extends Handler.Abstract {
    public static final String SERVER_HEADER_KEY = "X-Server";
    public static final String SERVER_HEADER_VALUE = "SDCri";

    private static final Logger LOG = LogManager.getLogger();

    private final String mediaType;
    private final HttpHandler handler;
    private final Logger instanceLogger;
    private final boolean chunkedTransfer;
    private final String charset;

    @AssistedInject
    CustomJettyHttpServerHandler(
            @Assisted String mediaType,
            @Assisted HttpHandler handler,
            @Named(CommonConfig.INSTANCE_IDENTIFIER) String frameworkIdentifier,
            @Named(DpwsConfig.ENFORCE_HTTP_CHUNKED_TRANSFER) boolean chunkedTransfer,
            @Named(DpwsConfig.HTTP_CONTENT_TYPE_CHARSET) String charset) {
        this.instanceLogger = InstanceLogger.wrapLogger(LOG, frameworkIdentifier);
        this.mediaType = mediaType;
        this.handler = handler;
        this.chunkedTransfer = chunkedTransfer;
        this.charset = charset;
    }

    @Override
    public boolean handle(Request request, Response response, Callback callback) throws Exception {
        final Supplier<String> remoteNodeInfo = () -> getRemoteNodeInfo(request);
        var transactionIdOpt = Optional.ofNullable(request.getAttribute(CommunicationLog.MessageType.REQUEST.name()));
        var transactionId = (String) transactionIdOpt.orElse("");

        instanceLogger.debug("{}: Request to {}", remoteNodeInfo::get, request::getHttpURI);
        var responseHeaders = response.getHeaders();
        response.setStatus(HttpStatus.OK_200);
        responseHeaders.put(HttpHeader.CONTENT_TYPE, "%s; %s".formatted(mediaType, charset));
        responseHeaders.put(SERVER_HEADER_KEY, SERVER_HEADER_VALUE);

        var input = Content.Source.asInputStream(request);

        ByteArrayOutputStream tempOut = new ByteArrayOutputStream();

        var requestHttpApplicationInfo =
                new HttpApplicationInfo(CustomJettyUtil.getRequestHeaders(request), transactionId, null);

        try {
            var localAddress =
                    (InetSocketAddress) request.getConnectionMetaData().getLocalSocketAddress();
            var remoteAddress =
                    (InetSocketAddress) request.getConnectionMetaData().getRemoteSocketAddress();
            handler.handle(
                    input,
                    tempOut,
                    new CommunicationContext(
                            requestHttpApplicationInfo,
                            new TransportInfo(
                                    request.getHttpURI().getScheme(),
                                    localAddress.getHostString(),
                                    localAddress.getPort(),
                                    remoteAddress.getHostString(),
                                    remoteAddress.getPort(),
                                    getX509Certificates(request, request.isSecure()))));
        } catch (HttpException e) {
            instanceLogger.warn(
                    "{}: An HTTP exception occurred during HTTP request processing. Error message: {}",
                    remoteNodeInfo::get,
                    e::getMessage);
            instanceLogger.trace(
                    () -> String.format(
                            "%s: An HTTP exception occurred during HTTP request processing", remoteNodeInfo.get()),
                    e);
            response.setStatus(e.getStatusCode());
            if (!e.getMessage().isEmpty()) {
                tempOut.write(e.getMessage().getBytes());
            }
            callback.failed(e);
            return false;
        }

        final byte[] tempOutValue = tempOut.toByteArray();

        if (chunkedTransfer) {
            responseHeaders.put("Transfer-Encoding", "chunked");
        } else {
            responseHeaders.put("Content-Length", String.valueOf(tempOutValue.length));
        }

        OutputStream output = Content.Sink.asOutputStream(response);
        output.write(tempOutValue);

        try {
            input.close();
            output.flush();
            output.close();
        } catch (IOException e) {
            instanceLogger.error(
                    "{}: Could not close input/output streams from incoming HTTP request to {}. Reason: {}",
                    remoteNodeInfo::get,
                    request::getHttpURI,
                    e::getMessage);
            instanceLogger.trace(
                    () -> String.format(
                            "%s: Could not close input/output streams from incoming HTTP request to %s",
                            remoteNodeInfo.get(), request.getHttpURI()),
                    e);
        }

        callback.succeeded();
        return true;
    }

    /**
     * Static helper function to get X509 certificate information from an HTTP servlet.
     *
     * @param request   request data.
     * @param expectTLS causes this function to return an empty list if set to false.
     * @return a list of {@link X509Certificate} containers.
     * @throws IOException in case the certificate information does not match the expected type, which is an array of
     *                     {@link X509Certificate}.
     */
    static List<X509Certificate> getX509Certificates(Request request, boolean expectTLS) throws IOException {
        if (!expectTLS) {
            return Collections.emptyList();
        }

        var anonymousCertificates = request.getAttribute("org.eclipse.jetty.server.x509");
        if (anonymousCertificates == null) {
            LOG.error(
                    "{}: Certificate information is missing from HTTP request data", () -> getRemoteNodeInfo(request));
            throw new IOException("Certificate information is missing from HTTP request data");
        } else {
            if (anonymousCertificates instanceof X509) {
                return List.of(((X509) anonymousCertificates).getCertificate());
            } else {
                LOG.error("Certificate information is of an unexpected type: {}", anonymousCertificates.getClass());
                throw new IOException(String.format(
                        "Certificate information is of an unexpected type: %s", anonymousCertificates.getClass()));
            }
        }
    }

    private static String getRemoteNodeInfo(Request request) {
        return String.format(
                "%s://%s:%s",
                request.getHttpURI().getScheme(),
                request.getHttpURI().getHost(),
                request.getHttpURI().getPort());
    }
}
