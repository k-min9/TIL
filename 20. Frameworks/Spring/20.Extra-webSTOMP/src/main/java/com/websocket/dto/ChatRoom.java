package com.websocket.dto;

import lombok.Data;

import java.io.Serializable;
import java.util.UUID;

/**
 * 채팅방 구현
 * 자바 직렬화 : 내부 객체 또는 데이터를 외부의 자바 시스템에서도 사용할 수 있게 바이트 형태로 변환
 */
@Data
public class ChatRoom implements Serializable {

    private static final long serialVersionUID = 6494678977089006639L;

    private String roomId;
    private String name;

    public static ChatRoom create(String name) {
        ChatRoom chatRoom = new ChatRoom();
        chatRoom.roomId = UUID.randomUUID().toString();
        chatRoom.name = name;
        return chatRoom;
    }

}
