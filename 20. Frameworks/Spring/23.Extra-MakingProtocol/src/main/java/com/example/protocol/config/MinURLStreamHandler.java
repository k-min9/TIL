package com.example.protocol.config;

import java.io.IOException;
import java.net.Proxy;
import java.net.URL;
import java.net.URLConnection;
import java.net.URLStreamHandler;
import java.util.StringTokenizer;

public class MinURLStreamHandler extends URLStreamHandler {

    String username;

    @Override
    protected URLConnection openConnection(URL u) throws IOException {
        return new MinURLConnection(u);
    }

    /**
     * min://kk@kk.kk.edu 같은 느낌낌
    * @param u
     * @param spec
     * @param start
     * @param limit
     */
    @Override
    protected void parseURL(URL u, String spec, int start, int limit) {
        StringTokenizer st = new StringTokenizer(spec.substring(start), ":@", false);
        String protocol = st.nextToken();
        String file = st.nextToken();
        String host = st.nextToken();
        String ref = null;
        int port = 25;

        setURL(u, protocol, host, port, file, ref);
    }

    @Override
    protected String toExternalForm(URL u) {
        return "min:" + u.getFile() + "@" + u.getHost();
    }
}
