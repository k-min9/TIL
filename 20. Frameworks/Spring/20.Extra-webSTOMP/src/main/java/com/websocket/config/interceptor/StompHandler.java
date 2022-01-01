package com.websocket.config.interceptor;

import com.websocket.service.jwt.JwtTokenProvider;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.context.annotation.Configuration;
import org.springframework.messaging.Message;
import org.springframework.messaging.MessageChannel;
import org.springframework.messaging.simp.stomp.StompCommand;
import org.springframework.messaging.simp.stomp.StompHeaderAccessor;
import org.springframework.messaging.support.ChannelInterceptor;

/**
 * Websocket 연결 시 요청 header의 jwt token 유효성을 검증하는 코드를 다음과 같이 추가
 * 유효하지 않을 경우 예외 처리
 */
//@Slf4j
@RequiredArgsConstructor
@Configuration
public class StompHandler implements ChannelInterceptor {

    private final JwtTokenProvider jwtTokenProvider;

    // websocket을 통해 들어온 요청이 처리 되기전 실행된다.
    @Override
    public Message<?> preSend(Message<?> message, MessageChannel channel) {

        StompHeaderAccessor accessor = StompHeaderAccessor.wrap(message);

        // websocket 연결 요청시, 헤더의 jwt token 검증
        if (StompCommand.CONNECT == accessor.getCommand()) {
            jwtTokenProvider.validateToken(accessor.getFirstNativeHeader("token"));  // 뷰에서 쓸 토큰 헤더 나중에 정하자!
        }
        return message;
    }
}
