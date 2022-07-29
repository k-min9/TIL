package com.example.protocol.config;

import java.net.URLStreamHandler;
import java.net.URLStreamHandlerFactory;

/**
 * https:// 식으로 min:// 을 만들어보자
 *  URL.setURLStreamHandlerFactory(URLStreamHandlerFactory arg)를 통해서 할 수 있다.
 */
public class MinURLStreamHandlerFactory implements URLStreamHandlerFactory {

    @Override
    public URLStreamHandler createURLStreamHandler(String protocol) {
        try {
            // 내가 만든 프로토콜을 리턴
            if(protocol.equals("cube") == true) {
                return new MinURLStreamHandler();
            }

            // 아니라면 원래 코드 수행
            String className = "sun.net.www.protocol." + protocol + ".Handler";
            Class<?> type = Class.forName(className);
            if(type == null) { return null; }
            return (URLStreamHandler)type.newInstance();
        } catch(Exception e) {
            return null;
        }
    }
}
