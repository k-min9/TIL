package com.websocket.dto;

import com.websocket.service.ChatService;
import lombok.Builder;
import lombok.Data;
import org.springframework.web.socket.WebSocketSession;

import java.util.HashSet;
import java.util.Set;

// 채팅 방 구현
@Data
public class ChatRoomDto {

    private String roomId;
    private String name;
    private Set<WebSocketSession> sessions = new HashSet<>();  // 입장한 클라이언트들의 정보 리스트(멤버 필드)

    @Builder  // ???
    public ChatRoomDto(String roomId, String name) {
        this.roomId = roomId;
        this.name = name;
    }

    // 채팅방에 입장하기, 대화하기 기능등을 분기처리
    // 입장 -> 세션 정보에 클라이언트의 세션 리스트를 추가
    // 대화하기 -> 채팅룸의 모든 세션에 메시지를 발송
    public void handleActions(WebSocketSession session, ChatMessageDto chatMessage, ChatService chatService) {
        if (chatMessage.getType().equals(ChatMessageDto.MessageType.ENTER)) {
            sessions.add(session);
            chatMessage.setMessage(chatMessage.getSender() + "님이 입장했습니다.");
        }
        sendMessage(chatMessage, chatService);
    }

    public <T> void sendMessage(T message, ChatService chatService) {
        sessions.parallelStream().forEach(session -> chatService.sendMessage(session, message));
    }

}
