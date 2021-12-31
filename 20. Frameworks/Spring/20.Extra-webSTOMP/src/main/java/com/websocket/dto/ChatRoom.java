package com.websocket.dto;

import lombok.Data;

import java.util.UUID;

// 채팅 방 구현
@Data
public class ChatRoom {

    private String roomId;
    private String name;

    public static ChatRoom create(String name) {
        ChatRoom chatRoom = new ChatRoom();
        chatRoom.roomId = UUID.randomUUID().toString();
        chatRoom.name = name;
        return chatRoom;
    }

}
