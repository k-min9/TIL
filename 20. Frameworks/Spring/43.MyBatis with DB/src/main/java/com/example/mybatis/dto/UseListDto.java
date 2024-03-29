package com.example.mybatis.dto;

import lombok.Getter;
import lombok.Setter;

import java.util.Arrays;
import java.util.List;

@Getter @Setter
public class UseListDto {

    private String use_no;
    private int use_distance;
    private int use_time;
    private String use_start_dt;
    private String use_end_dt;
    private String pay_datetime;
    private int card_pay;
    private int point_pay;
    private List<String> pay_method;
    private Double pay_discount;  // primitive이면 기본값이 0.0으로 들어가므로 null을 위해 래퍼클래스 Double!

}
