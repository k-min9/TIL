package com.websocket.controller;

import com.websocket.dto.ChatMessage;
import lombok.RequiredArgsConstructor;
import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.simp.SimpMessageSendingOperations;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;

@RequiredArgsConstructor
@Controller
@CrossOrigin(origins="*")
public class ChatController {

    private final SimpMessageSendingOperations messagingTemplate;

    // "/pub/chat/message"로 들어오는 메시징을 처리
    @MessageMapping("/chat/message")  // websocket으로 들어오는 메시지 발행(/sub/chat/room/{roomId}로 메시지를 send)
    public void message(ChatMessage message) {
        if (ChatMessage.MessageType.ENTER.equals(message.getType()))
            message.setMessage(message.getSender() + "님이 입장하셨습니다.");
        messagingTemplate.convertAndSend("/sub/chat/room/" + message.getRoomId(), message);
    }
}
