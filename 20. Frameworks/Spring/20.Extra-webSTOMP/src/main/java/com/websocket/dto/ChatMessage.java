package com.websocket.dto;

import lombok.Builder;
import lombok.Data;

// 채팅 메시지 구현
@Data
public class ChatMessage {

    // 메시지 타입 : 채팅방 입장, 채팅방 메시지보내기, 채팅방 나가기
    public enum MessageType {
        ENTER, TALK, QUIT
    }
    private MessageType type; // 메시지 타입
    private String roomId; // 방번호
    private String sender; // 메시지 보낸사람
    private String message; // 메시지
    private long userCount;  // 채팅방 인원수, 채팅방 내에서 메시지가 전달될때 인원수 갱신시 사용

    @Builder
    public ChatMessage(MessageType type, String roomId, String sender, String message, long userCount) {
        this.type = type;
        this.roomId = roomId;
        this.sender = sender;
        this.message = message;
        this.userCount = userCount;
    }
    
}
