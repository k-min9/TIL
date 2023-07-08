package com.example.mybatis.dto;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class PayMethodDto {
    private String code;
    private String id;  // 카드, 포인트
}
