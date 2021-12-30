package com.websocket.config;

import com.websocket.handler.WebsocketChatHandler;
import lombok.RequiredArgsConstructor;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.socket.config.annotation.EnableWebSocket;
import org.springframework.web.socket.config.annotation.WebSocketConfigurer;
import org.springframework.web.socket.config.annotation.WebSocketHandlerRegistry;

@RequiredArgsConstructor
@Configuration
@EnableWebSocket
public class WebsocketConfig implements WebSocketConfigurer {

    private final WebsocketChatHandler websocketChatHandler;

    // 여기까지하면 localhost:8080/ws/chat으로 커넥션 연결하고 메시지 통신할 수 있음
    @Override
    public void registerWebSocketHandlers(WebSocketHandlerRegistry registry) {
        registry.addHandler(websocketChatHandler, "/ws/chat").setAllowedOrigins("*");
    }
}
