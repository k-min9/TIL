package com.websocket.service.pubsub;

import com.websocket.dto.ChatMessage;
import lombok.RequiredArgsConstructor;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.listener.ChannelTopic;
import org.springframework.stereotype.Service;

/**
 * Redis 발행 서비스 구현
 * Redis에서는 공통 주제(Topic)에 대하여 구독자(subscriber)에게 메시지를 발행(publish)
 * Topic : 채팅방
 * pub : 대화하기
 * sub : 대화보기
 */
@RequiredArgsConstructor
@Service
public class RedisPublisher {

    private final RedisTemplate<String, Object> redisTemplate;

    public void publish(ChannelTopic topic, ChatMessage message) {
        redisTemplate.convertAndSend(topic.getTopic(), message);
    }
}