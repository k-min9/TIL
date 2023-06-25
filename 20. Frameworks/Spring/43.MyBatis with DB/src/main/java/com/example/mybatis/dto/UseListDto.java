package com.example.mybatis.dto;

import lombok.Getter;
import lombok.Setter;

@Getter @Setter
public class UseListDto {

    private String use_no = "use_no_1";
    private int use_distance = 10;
    private int use_time = 100;
    private String use_start_dt = "2023-01-01";
    private String use_end_dt = "2023-01-23";
    private String pay_datetime = "2023-01-01";
    private int card_pay = 1;
    private int point_pay = 2;
}
