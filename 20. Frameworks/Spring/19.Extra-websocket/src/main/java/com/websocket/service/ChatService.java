package com.websocket.service;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.websocket.dto.ChatRoomDto;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.web.socket.TextMessage;
import org.springframework.web.socket.WebSocketSession;

import javax.annotation.PostConstruct;
import java.io.IOException;
import java.util.*;

@Slf4j
@RequiredArgsConstructor
@Service
public class ChatService {

    private final ObjectMapper objectMapper;
    private Map<String, ChatRoomDto> chatRooms;

    @PostConstruct
    private void init() {
        chatRooms = new LinkedHashMap<>();  // 차후 외부저장소(JPA)로 변경 필요
    }

    // 채팅방 전체 조회
    public List<ChatRoomDto> findAllRoom() {
        return new ArrayList<>(chatRooms.values());
    }

    // 채팅방 단일 조회
    public ChatRoomDto findRoomById(String roomId) {
        return chatRooms.get(roomId);
    }

    // 채팅방 생성 : random UUID를 구별 ID로 가지는 채팅방 객체 생성 -> 이것도 빌더가 아니라 나중에 고쳐야겠다.
    public ChatRoomDto createRoom(String name) {
        String randomId = UUID.randomUUID().toString();
        ChatRoomDto chatRoom = ChatRoomDto.builder()
                .roomId(randomId)
                .name(name)
                .build();
        chatRooms.put(randomId, chatRoom);
        return chatRoom;
    }

    // 메시지 발송 : 지정한 Websocket 세션에 메시지를 발송
    public <T> void sendMessage(WebSocketSession session, T message) {
        try {
            session.sendMessage(new TextMessage(objectMapper.writeValueAsString(message)));
        } catch (IOException e) {
            log.error(e.getMessage(), e);
        }
    }
}