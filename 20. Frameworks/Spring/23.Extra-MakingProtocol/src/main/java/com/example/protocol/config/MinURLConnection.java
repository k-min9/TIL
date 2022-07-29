package com.example.protocol.config;

import java.io.IOException;
import java.io.InputStream;
import java.net.Socket;
import java.net.URL;
import java.net.URLConnection;

public class MinURLConnection extends URLConnection {

    Socket theConnection = null;
    public final static int defaultPort = 19;

    public String getContentType() {
        return "text/plain";
    }

    public MinURLConnection(URL u) {
        super(u);
    }

    public synchronized InputStream getInputStream() throws IOException {
        if (!connected) {
            connect();
        }

        return theConnection.getInputStream();
    }

    @Override
    public void connect() throws IOException {

        int port;

        if(!connected) {
            port = url.getPort();
            if(port < 0) {
                port = defaultPort;
            }
            theConnection = new Socket(url.getHost(), port);
            connected = true;
        }

    }

}
