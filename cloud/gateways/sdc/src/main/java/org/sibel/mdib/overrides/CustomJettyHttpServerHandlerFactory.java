package org.sibel.mdib.overrides;

import org.somda.sdc.dpws.http.HttpHandler;

/**
 * Creates {@linkplain CustomJettyHttpServerHandler} instances.
 */
public interface CustomJettyHttpServerHandlerFactory {

    /**
     * Instantiates {@linkplain CustomJettyHttpServerHandler} with the given objects and injected objects.
     *
     * @param mediaType media type of transmitted content
     * @param handler   to handle incoming requests
     * @return a new {@linkplain CustomJettyHttpServerHandler}
     */
    CustomJettyHttpServerHandler create(String mediaType, HttpHandler handler);
}
