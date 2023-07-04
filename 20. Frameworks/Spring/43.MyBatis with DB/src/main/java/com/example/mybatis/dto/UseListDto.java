package com.example.mybatis.dto;

import lombok.Getter;
import lombok.Setter;

import java.util.List;

@Getter @Setter
public class UseListDto {

    private String use_no = "use_no_1";
    private int use_distance = 10;
    private int use_time = 100;
    private String use_start_dt = "2023-01-01 11:00:00";
    private String use_end_dt = "2023-01-23 23:00:00";
    private String pay_datetime = "2023-01-01";
    private int card_pay = 1;
    private int point_pay = 2;
    private List<String> pay_method;
}
