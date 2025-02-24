package org.sibel.mdib.overrides;

import com.google.common.collect.ArrayListMultimap;
import com.google.common.collect.ListMultimap;
import java.util.stream.Stream;
import org.eclipse.jetty.server.Request;

/**
 * Jetty utilities.
 */
public class CustomJettyUtil {
    /**
     * Returns all available headers from an incoming request.
     *
     * @param request to extract headers from.
     * @return extracted headers as a multimap, without duplicates.
     */
    static ListMultimap<String, String> getRequestHeaders(Request request) {
        ListMultimap<String, String> requestHeaderMap = ArrayListMultimap.create();
        var nameIter = request.getHeaders().getFieldNamesCollection().iterator();
        Stream.generate(() -> null) // what
                .takeWhile(x -> nameIter.hasNext())
                .map(n -> nameIter.next().toLowerCase())
                // filter duplicates which occur because of capitalization
                .distinct()
                .forEach(headerName -> {
                    var headers = request.getHeaders().getValues(headerName);
                    headers.asIterator().forEachRemaining(header -> requestHeaderMap.put(headerName, header));
                });
        return requestHeaderMap;
    }
}
