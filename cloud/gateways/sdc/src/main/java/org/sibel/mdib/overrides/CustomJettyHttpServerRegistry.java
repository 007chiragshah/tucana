package org.sibel.mdib.overrides;

import com.google.common.util.concurrent.AbstractIdleService;
import com.google.inject.Inject;
import com.google.inject.name.Named;
import java.io.IOException;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.UnknownHostException;
import java.security.KeyManagementException;
import java.security.KeyStoreException;
import java.security.NoSuchAlgorithmException;
import java.security.UnrecoverableKeyException;
import java.security.cert.CertificateException;
import java.time.Duration;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import javax.annotation.Nullable;
import javax.net.ssl.HostnameVerifier;
import javax.net.ssl.SSLContext;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.eclipse.jetty.http.*;
import org.eclipse.jetty.server.*;
import org.eclipse.jetty.server.handler.ContextHandler;
import org.eclipse.jetty.server.handler.ContextHandlerCollection;
import org.eclipse.jetty.server.handler.gzip.GzipHandler;
import org.eclipse.jetty.server.internal.HttpConnection;
import org.eclipse.jetty.util.ssl.SslContextFactory;
import org.somda.sdc.common.CommonConfig;
import org.somda.sdc.common.logging.InstanceLogger;
import org.somda.sdc.dpws.CommunicationLog;
import org.somda.sdc.dpws.DpwsConfig;
import org.somda.sdc.dpws.crypto.CryptoConfig;
import org.somda.sdc.dpws.crypto.CryptoConfigurator;
import org.somda.sdc.dpws.crypto.CryptoSettings;
import org.somda.sdc.dpws.http.HttpHandler;
import org.somda.sdc.dpws.http.HttpServerRegistry;
import org.somda.sdc.dpws.http.HttpUriBuilder;
import org.somda.sdc.dpws.soap.SoapConstants;

/**
 * {@linkplain HttpServerRegistry} implementation based on Jetty HTTP servers.
 */
public class CustomJettyHttpServerRegistry extends AbstractIdleService implements HttpServerRegistry {
    public static final String CUSTOMIZER_VERIFIED_ATTRIBUTE = "customizer.verified";

    private static final Logger LOG = LogManager.getLogger();

    private static final String URI_CONVERSION_ERROR_MSG = "Unexpected URI conversion error";

    private CustomJettyHttpServerHandlerFactory jettyHttpServerHandlerFactory;

    private final Logger instanceLogger;
    private final Map<String, Server> serverRegistry;
    private final Map<String, CustomJettyHttpServerHandler> handlerRegistry;
    private final Map<String, ContextHandler> contextWrapperRegistry;
    private final Map<Server, ContextHandlerCollection> contextHandlerMap;
    private final Lock registryLock;
    private final HttpUriBuilder uriBuilder;
    private final boolean enableGzipCompression;
    private final int minCompressionSize;
    private final String[] tlsProtocols;
    private final String[] enabledCiphers;
    private final HostnameVerifier hostnameVerifier;
    private final boolean enableHttp;
    private final boolean enableHttps;
    private final Duration connectionTimeout;
    private SSLContext sslContext;

    @Inject
    CustomJettyHttpServerRegistry(
            HttpUriBuilder uriBuilder,
            CryptoConfigurator cryptoConfigurator,
            @Nullable @Named(CryptoConfig.CRYPTO_SETTINGS) CryptoSettings cryptoSettings,
            CustomJettyHttpServerHandlerFactory jettyHttpServerHandlerFactory,
            @Named(DpwsConfig.HTTP_GZIP_COMPRESSION) boolean enableGzipCompression,
            @Named(DpwsConfig.HTTP_RESPONSE_COMPRESSION_MIN_SIZE) int minCompressionSize,
            @Named(CryptoConfig.CRYPTO_TLS_ENABLED_VERSIONS) String[] tlsProtocols,
            @Named(CryptoConfig.CRYPTO_TLS_ENABLED_CIPHERS) String[] enabledCiphers,
            @Named(CryptoConfig.CRYPTO_DEVICE_HOSTNAME_VERIFIER) HostnameVerifier hostnameVerifier,
            @Named(DpwsConfig.HTTPS_SUPPORT) boolean enableHttps,
            @Named(DpwsConfig.HTTP_SUPPORT) boolean enableHttp,
            @Named(DpwsConfig.HTTP_SERVER_CONNECTION_TIMEOUT) Duration connectionTimeout,
            @Named(CommonConfig.INSTANCE_IDENTIFIER) String frameworkIdentifier) {
        this.instanceLogger = InstanceLogger.wrapLogger(LOG, frameworkIdentifier);
        this.uriBuilder = uriBuilder;
        this.jettyHttpServerHandlerFactory = jettyHttpServerHandlerFactory;
        this.enableGzipCompression = enableGzipCompression;
        this.minCompressionSize = minCompressionSize;
        this.tlsProtocols = tlsProtocols;
        this.enabledCiphers = enabledCiphers;
        this.hostnameVerifier = hostnameVerifier;
        this.enableHttps = enableHttps;
        this.enableHttp = enableHttp;
        this.connectionTimeout = connectionTimeout;
        serverRegistry = new HashMap<>();
        handlerRegistry = new HashMap<>();
        contextHandlerMap = new HashMap<>();
        contextWrapperRegistry = new HashMap<>();
        registryLock = new ReentrantLock();
        configureSsl(cryptoConfigurator, cryptoSettings);

        if (!this.enableHttp && !this.enableHttps) {
            throw new RuntimeException("Http and https are disabled, cannot continue");
        }
    }

    @Override
    protected void startUp() throws Exception {
        // nothing to do here - servers will be started on demand
        instanceLogger.info("{} is running", getClass().getSimpleName());
    }

    @Override
    protected void shutDown() throws Exception {
        instanceLogger.info("Shut down running HTTP servers");
        registryLock.lock();
        try {

            serverRegistry.forEach((uri, server) -> {
                try {

                    server.stop();
                    instanceLogger.info("Shut down HTTP server at {}", uri);

                    ContextHandlerCollection contextHandlerCollection = contextHandlerMap.remove(server);
                    if (contextHandlerCollection != null) {
                        contextHandlerCollection.stop();
                        instanceLogger.info("Shut down HTTP context handler collection at {}", uri);
                    }

                    this.handlerRegistry.forEach((handlerUri, handler) -> {
                        try {
                            handler.stop();
                            // CHECKSTYLE.OFF: IllegalCatch
                        } catch (Exception e) {
                            // CHECKSTYLE.ON: IllegalCatch
                            instanceLogger.warn("HTTP handler could not be stopped properly", e);
                        }
                    });
                    handlerRegistry.clear();

                    contextWrapperRegistry.forEach((contextPath, wrapper) -> {
                        try {
                            wrapper.stop();
                            // CHECKSTYLE.OFF: IllegalCatch
                        } catch (Exception e) {
                            // CHECKSTYLE.ON: IllegalCatch
                            instanceLogger.warn("HTTP handler wrapper could not be stopped properly", e);
                        }
                    });
                    contextWrapperRegistry.clear();
                    // CHECKSTYLE.OFF: IllegalCatch
                } catch (Exception e) {
                    // CHECKSTYLE.ON: IllegalCatch
                    instanceLogger.warn("HTTP server could not be stopped properly", e);
                }
            });

            serverRegistry.clear();

        } finally {
            registryLock.unlock();
        }
    }

    // TODO: 2.0.0 - return all created URIs, i.e. http and https
    @Override
    public String initHttpServer(String schemeAndAuthority) {
        registryLock.lock();
        try {
            var server = makeHttpServer(schemeAndAuthority);
            var uriString = server.getURI().toString();
            if (uriString.endsWith("/")) {
                uriString = uriString.substring(0, uriString.length() - 1);
            }
            var serverUri = URI.create(uriString);
            var requestedUri = URI.create(schemeAndAuthority);
            if (!serverUri.getScheme().equals(requestedUri.getScheme())) {
                try {
                    serverUri = replaceScheme(serverUri, requestedUri.getScheme());
                } catch (URISyntaxException e) {
                    instanceLogger.error(
                            "Unexpected error while creating server uri value with uri {} and new scheme {} value: {}",
                            serverUri,
                            requestedUri.getScheme(),
                            e.getMessage());
                    instanceLogger.trace(
                            "Unexpected error while creating server uri value with uri {} and new scheme {} value",
                            serverUri,
                            requestedUri.getScheme(),
                            e);
                }
            }
            return serverUri.toString();
        } finally {
            registryLock.unlock();
        }
    }

    // TODO: 2.0.0 - return all created URIs, i.e. http and https
    @Override
    public String registerContext(String schemeAndAuthority, String contextPath, HttpHandler handler) {
        return registerContext(schemeAndAuthority, contextPath, SoapConstants.MEDIA_TYPE_SOAP, handler);
    }

    // TODO: 2.0.0 - return all created URIs, i.e. http and https
    @Override
    public String registerContext(
            String schemeAndAuthority,
            String contextPath,
            @Nullable CommunicationLog communicationLog,
            HttpHandler handler) {
        return registerContext(
                schemeAndAuthority, contextPath, SoapConstants.MEDIA_TYPE_SOAP, communicationLog, handler);
    }

    // TODO: 2.0.0 - return all created URIs, i.e. http and https
    @Override
    public String registerContext(
            String schemeAndAuthority, String contextPath, String mediaType, HttpHandler handler) {
        return registerContext(schemeAndAuthority, contextPath, mediaType, null, handler);
    }

    // TODO: 2.0.0 - return all created URIs, i.e. http and https
    @Override
    public String registerContext(
            String schemeAndAuthority,
            String contextPath,
            String mediaType,
            @Nullable CommunicationLog communicationLog,
            HttpHandler handler) {
        if (!contextPath.startsWith("/")) {
            throw new RuntimeException(
                    String.format("Context path needs to start with a slash, but is %s", contextPath));
        }

        registryLock.lock();
        try {
            Server server = makeHttpServer(schemeAndAuthority);
            String mapKey;
            try {
                mapKey = makeMapKey(server.getURI().toString(), contextPath);
            } catch (UnknownHostException e) {
                instanceLogger.error(URI_CONVERSION_ERROR_MSG, e);
                throw new RuntimeException(URI_CONVERSION_ERROR_MSG, e);
            }
            URI mapKeyUri = URI.create(mapKey);

            var endpointHandler = this.jettyHttpServerHandlerFactory.create(mediaType, handler);

            ContextHandler context = new ContextHandler(contextPath);
            context.setHandler(endpointHandler);
            context.setAllowNullPathInContext(true);

            this.handlerRegistry.put(mapKeyUri.toString(), endpointHandler);
            this.contextWrapperRegistry.put(contextPath, context);

            ContextHandlerCollection contextHandler = this.contextHandlerMap.get(server);
            contextHandler.addHandler(context);

            context.start();

            // use requested scheme for response
            var contextUri =
                    replaceScheme(mapKeyUri, URI.create(schemeAndAuthority).getScheme());
            return contextUri.toString();
            // CHECKSTYLE.OFF: IllegalCatch
        } catch (Exception e) {
            // CHECKSTYLE.ON: IllegalCatch
            instanceLogger.error("Registering context {} failed.", contextPath, e);
            throw new RuntimeException(e);
        } finally {
            registryLock.unlock();
        }
    }

    @Override
    public void unregisterContext(String schemeAndAuthority, String contextPath) {
        registryLock.lock();
        try {
            String serverRegistryKey;
            String httpHandlerRegistryKey;

            try {
                serverRegistryKey = makeMapKey(schemeAndAuthority);
                httpHandlerRegistryKey = makeMapKey(schemeAndAuthority, contextPath);
            } catch (UnknownHostException e) {
                instanceLogger.error(URI_CONVERSION_ERROR_MSG, e);
                throw new RuntimeException(URI_CONVERSION_ERROR_MSG, e);
            }

            Optional.ofNullable(serverRegistry.get(serverRegistryKey)).ifPresent(httpServer -> {
                Optional.ofNullable(handlerRegistry.get(httpHandlerRegistryKey)).ifPresent(handlerWrapper -> {
                    instanceLogger.info("Unregister context path '{}'", contextPath);
                    handlerRegistry.remove(httpHandlerRegistryKey);
                    ContextHandler removedHandler = contextWrapperRegistry.remove(contextPath);
                    ContextHandlerCollection servletContextHandler = contextHandlerMap.get(httpServer);
                    servletContextHandler.removeHandler(removedHandler);
                });

                if (handlerRegistry.isEmpty()) {
                    instanceLogger.info(
                            "No further HTTP handlers active. Shutdown HTTP server at '{}'", schemeAndAuthority);
                    try {
                        httpServer.stop();
                        // CHECKSTYLE.OFF: IllegalCatch
                    } catch (Exception e) {
                        // CHECKSTYLE.ON: IllegalCatch
                        instanceLogger.error("Could not stop HTTP server", e);
                    }
                    serverRegistry.remove(serverRegistryKey);
                }
            });
        } finally {
            registryLock.unlock();
        }
    }

    private void configureSsl(CryptoConfigurator cryptoConfigurator, @Nullable CryptoSettings cryptoSettings) {
        if (cryptoSettings == null) {
            sslContext = null;
            return;
        }

        try {
            sslContext = cryptoConfigurator.createSslContextFromCryptoConfig(cryptoSettings);
        } catch (IllegalArgumentException
                | KeyStoreException
                | UnrecoverableKeyException
                | CertificateException
                | NoSuchAlgorithmException
                | IOException
                | KeyManagementException e) {
            instanceLogger.warn("Could not read server crypto config, fallback to system properties");
            sslContext = cryptoConfigurator.createSslContextFromSystemProperties();
        }
    }

    private Server makeHttpServer(String uri) {
        String mapKey;
        try {
            mapKey = makeMapKey(uri);
        } catch (UnknownHostException e) {
            instanceLogger.error(URI_CONVERSION_ERROR_MSG, e);
            throw new RuntimeException(URI_CONVERSION_ERROR_MSG, e);
        }

        Optional<Server> oldServer = Optional.ofNullable(serverRegistry.get(mapKey));
        if (oldServer.isPresent()) {
            instanceLogger.debug(
                    "Re-use running HTTP server from URI: {}",
                    oldServer.get().getURI().getHost());
            return oldServer.get();
        }

        instanceLogger.debug("Init new HTTP server from URI: {}", uri);
        Server httpServer = createHttpServer(URI.create(uri));
        try {
            httpServer.start();
            // CHECKSTYLE.OFF: IllegalCatch
        } catch (Exception e) {
            // CHECKSTYLE.ON: IllegalCatch
            throw new RuntimeException(e);
        }

        var serverUri = httpServer.getURI().toString();
        try {
            serverRegistry.put(makeMapKey(serverUri), httpServer);
        } catch (UnknownHostException e) {
            instanceLogger.error(URI_CONVERSION_ERROR_MSG, e);
            throw new RuntimeException(URI_CONVERSION_ERROR_MSG, e);
        }
        instanceLogger.debug("New HTTP server initialized: {}", uri);
        return httpServer;
    }

    private Server createHttpServer(URI uri) {
        instanceLogger.info("Setup HTTP server for address '{}'", uri);
        if (!isSupportedScheme(uri)) {
            throw new RuntimeException(
                    String.format("HTTP server setup failed. Unsupported scheme: %s", uri.getScheme()));
        }

        HttpConfiguration httpConfig = new HttpConfiguration();
        httpConfig.setSecureScheme(HttpScheme.HTTPS.asString());
        httpConfig.setHttpCompliance(HttpCompliance.RFC2616);

        var server = new Server(new InetSocketAddress(uri.getHost(), uri.getPort()));

        ContextHandlerCollection context = new ContextHandlerCollection();
        server.setHandler(context);
        this.contextHandlerMap.put(server, context);

        // Set up the RequestLogHandler
        var requestLog = new CustomRequestLog(new Slf4jRequestLogWriter(), CustomRequestLog.NCSA_FORMAT);
        server.setRequestLog(requestLog);

        // wrap the context handler in a gzip handler
        if (this.enableGzipCompression) {
            GzipHandler gzipHandler = new GzipHandler();
            gzipHandler.setIncludedMethods(
                    HttpMethod.PUT.asString(), HttpMethod.POST.asString(), HttpMethod.GET.asString());
            gzipHandler.setInflateBufferSize(2048);
            gzipHandler.setHandler(server.getHandler());
            gzipHandler.setMinGzipSize(minCompressionSize);
            gzipHandler.setIncludedMimeTypes(
                    "text/plain", "text/html", SoapConstants.MEDIA_TYPE_SOAP, SoapConstants.MEDIA_TYPE_WSDL);
            server.setHandler(gzipHandler);
        }

        if (sslContext != null && enableHttps) {
            SslContextFactory.Server contextFactory = new SslContextFactory.Server();
            contextFactory.setSslContext(sslContext);
            contextFactory.setNeedClientAuth(true);

            instanceLogger.debug("Enabled protocols: {}", () -> List.of(tlsProtocols));

            // reset excluded protocols to force only included protocols
            contextFactory.setExcludeProtocols();
            contextFactory.setIncludeProtocols(tlsProtocols);

            // reset excluded ciphers to force only included protocols
            contextFactory.setExcludeCipherSuites();
            contextFactory.setIncludeCipherSuites(enabledCiphers);

            SecureRequestCustomizer src = new SecureRequestCustomizer();
            // disable hostname validation, does not match sdc behavior
            src.setSniHostCheck(false);

            HttpConfiguration httpsConfig = new HttpConfiguration(httpConfig);
            HttpConfiguration.Customizer clientVerifier = (Request request, HttpFields.Mutable responseHeaders) -> {
                var connection = HttpConnection.getCurrentConnection();
                if (connection == null) {
                    instanceLogger.debug("Unable to obtain current http connection");
                    return request;
                }

                if (Boolean.TRUE.equals(request.getAttribute(CUSTOMIZER_VERIFIED_ATTRIBUTE))) {
                    instanceLogger.debug("Connection already verified");
                    return request;
                }
                var endpoint = connection.getEndPoint();
                var session = endpoint.getSslSessionData().sslSession();

                var socketAddress = endpoint.getLocalSocketAddress();
                if (socketAddress instanceof InetSocketAddress
                        && !hostnameVerifier.verify(((InetSocketAddress) socketAddress).getHostName(), session)) {
                    instanceLogger.debug("HostnameVerifier has filtered request, marking request as "
                            + "handled and aborting request");
                    endpoint.close(new Exception("HostnameVerifier has rejected request"));
                }

                request.setAttribute(CUSTOMIZER_VERIFIED_ATTRIBUTE, true);
                return request;
            };
            httpsConfig.addCustomizer(clientVerifier);
            httpsConfig.addCustomizer(src);

            var connectionFactory = new SslConnectionFactory(contextFactory, HttpVersion.HTTP_1_1.asString());
            ServerConnector httpsConnector;

            HttpConnectionFactory httpConnectionFactory = new HttpConnectionFactory(httpsConfig);

            if (enableHttp) {
                httpsConnector = new ServerConnector(
                        server,
                        new OptionalSslConnectionFactory(connectionFactory, HttpVersion.HTTP_1_1.asString()),
                        connectionFactory,
                        httpConnectionFactory);
            } else {
                httpsConnector = new ServerConnector(server, connectionFactory, httpConnectionFactory);
            }
            httpsConnector.setIdleTimeout(connectionTimeout.toMillis());
            httpsConnector.setHost(uri.getHost());
            httpsConnector.setPort(uri.getPort());

            server.setConnectors(new Connector[] {httpsConnector});
        } else {
            HttpConnectionFactory httpConnectionFactory = new HttpConnectionFactory();
            ServerConnector httpConnector;
            httpConnector = new ServerConnector(server, httpConnectionFactory);
            httpConnector.setIdleTimeout(connectionTimeout.toMillis());
            httpConnector.setHost(uri.getHost());
            httpConnector.setPort(uri.getPort());

            server.setConnectors(new Connector[] {httpConnector});
        }

        return server;
    }

    /*
     * Calculate http server map key:
     * - scheme is replaced by httpx to compare entries independent of used scheme
     * - host address is used instead of DNS name.
     *
     * throws UnknownHostException if host address cannot be resolved.
     */
    private String makeMapKey(String uri) throws UnknownHostException {
        URI parsedUri = URI.create(uri);
        InetAddress address = InetAddress.getByName(parsedUri.getHost());
        return uriBuilder.buildUri("httpx", address.getHostAddress(), parsedUri.getPort());
    }

    private String makeMapKey(String uri, String contextPath) throws UnknownHostException {
        return makeMapKey(uri) + contextPath;
    }

    private URI replaceScheme(URI baseUri, String scheme) throws URISyntaxException {
        return new URI(
                scheme,
                baseUri.getUserInfo(),
                baseUri.getHost(),
                baseUri.getPort(),
                baseUri.getPath(),
                baseUri.getQuery(),
                baseUri.getFragment());
    }

    private boolean isSupportedScheme(URI address) {
        return (enableHttp && HttpScheme.HTTP.asString().equalsIgnoreCase(address.getScheme()))
                || (enableHttps && HttpScheme.HTTPS.asString().equalsIgnoreCase(address.getScheme()));
    }
}
