package com.websocket.handler;

import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;
import org.springframework.web.socket.TextMessage;
import org.springframework.web.socket.WebSocketSession;
import org.springframework.web.socket.handler.TextWebSocketHandler;

@Slf4j  // 주의
@Component
public class WebsocketChatHandler extends TextWebSocketHandler {

    @Override
    protected void handleTextMessage(WebSocketSession session, TextMessage message) throws Exception {
        // Client로 부터 받은 메시지를 Console로그에 출력(로깅) // 디버깅용, 지금은 딱히 필요 없어보이는데
//        String payload = message.getPayload();
//        log.info("payload : {}", payload);

        // Client에 환영 메시지
        TextMessage textMessage = new TextMessage("채팅 서버에 오신것을 환영합니다.");
        session.sendMessage(textMessage);
    }
}
