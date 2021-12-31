package com.websocket.dto;

import lombok.Data;

// 채팅 메시지 구현
@Data
public class ChatMessage {

    // 메시지 타입 : 채팅방 입장, 채팅방 메시지보내기
    public enum MessageType {
        ENTER, TALK
    }
    private MessageType type; // 메시지 타입
    private String roomId; // 방번호
    private String sender; // 메시지 보낸사람
    private String message; // 메시지
    
}
