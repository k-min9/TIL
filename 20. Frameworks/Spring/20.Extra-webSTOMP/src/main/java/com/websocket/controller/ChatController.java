package com.websocket.controller;

import com.websocket.dto.ChatMessage;
import com.websocket.repository.ChatRoomRepository;
import com.websocket.service.jwt.JwtTokenProvider;
import lombok.RequiredArgsConstructor;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.listener.ChannelTopic;
import org.springframework.messaging.handler.annotation.Header;
import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.simp.SimpMessageSendingOperations;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;

@RequiredArgsConstructor
@Controller
public class ChatController {

    private final JwtTokenProvider jwtTokenProvider;

    private final RedisTemplate<String, Object> redisTemplate;
    private final ChannelTopic channelTopic;

    // "/pub/chat/message"로 들어오는 메시징을 처리
    @MessageMapping("/chat/message")  // websocket으로 들어오는 메시지 발행(/sub/chat/room/{roomId}로 메시지를 send)
    public void message(ChatMessage message, @Header("token") String token) {
        String nickname = jwtTokenProvider.getUsernameFromJwt(token);
        // 로그인 회원 정보로 대화명 설정
        message.setSender(nickname);
        // 채팅방 입장시에는 대화명과 메시지를 자동으로 세팅한다.
        if (ChatMessage.MessageType.ENTER.equals(message.getType())) {
            message.setSender("[알림]");
            message.setMessage(nickname + "님이 입장하셨습니다.");
        }
        // Websocket에 발행된 메시지를 redis로 발행한다(publish)
        // redisPublisher 대신, redisTemplate을 통해 바로 ChannelTopic으로 메시지를 발행하게 변경
        redisTemplate.convertAndSend(channelTopic.getTopic(), message);
    }
}
