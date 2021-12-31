package com.websocket.config;

import lombok.RequiredArgsConstructor;
import org.springframework.context.annotation.Configuration;
import org.springframework.messaging.simp.config.MessageBrokerRegistry;
import org.springframework.web.socket.config.annotation.*;

@RequiredArgsConstructor
@Configuration
@EnableWebSocketMessageBroker  // STOMP 사용 선언
public class WebsocketConfig implements WebSocketMessageBrokerConfigurer {

    @Override
    public void configureMessageBroker(MessageBrokerRegistry config) {
        //pub/sub 메시징을 구현
        config.enableSimpleBroker("/sub");  // 메시지를 구독하는 요청의 prefix는 /sub로 시작
        config.setApplicationDestinationPrefixes("/pub");  // 메시지를 발행하는 요청의 prefix는 /pub로 시작
    }

    /**
     * stomp websocket의 연결 endpoint는 /ws-stomp로 설정
     * 예상 접속 주소 : ws://localhost:8080/ws-stomp
     */
    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        registry.addEndpoint("/ws-stomp")
                .setAllowedOriginPatterns("*")
//                .setAllowedOrigins("*")  // 3년전은 이거로 CORS 통과가 됐는데 지금은 안됨. 차후 체크
                .withSockJS();
    }
}
