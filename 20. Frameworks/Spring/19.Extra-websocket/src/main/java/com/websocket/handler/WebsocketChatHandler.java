package com.websocket.handler;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.websocket.dto.ChatMessageDto;
import com.websocket.dto.ChatRoomDto;
import com.websocket.service.ChatService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;
import org.springframework.web.socket.TextMessage;
import org.springframework.web.socket.WebSocketSession;
import org.springframework.web.socket.handler.TextWebSocketHandler;

@Slf4j  // 주의
@Component
@RequiredArgsConstructor
public class WebsocketChatHandler extends TextWebSocketHandler {

    private final ObjectMapper objectMapper;
    private final ChatService chatService;

    @Override
    protected void handleTextMessage(WebSocketSession session, TextMessage message) throws Exception {
        String payload = message.getPayload();
        log.info("payload : {}", payload);  // 디버깅용 : Client로 부터 받은 메시지를 Console로그에 출력(로깅)

        // Client에 환영 메시지 (기존 방식)
//        TextMessage textMessage = new TextMessage("채팅 서버에 오신것을 환영합니다.");
//        session.sendMessage(textMessage);

        ChatMessageDto chatMessage = objectMapper.readValue(payload, ChatMessageDto.class);
        ChatRoomDto room = chatService.findRoomById(chatMessage.getRoomId());
        room.handleActions(session, chatMessage, chatService);

    }
}
