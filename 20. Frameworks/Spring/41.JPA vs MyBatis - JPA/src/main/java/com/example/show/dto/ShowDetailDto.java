package com.example.show.dto;

import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class ShowDetailDto {

  private String show_no;  // 공연 번호
  private int show_time = 0;  // 공연 길이
  private String show_start_dt; // 시작시간
  private String show_end_dt; // 종료시간
  private String show_pay_dt; // 결제시간
  private int card_pay; // 카드 결제 금액
  private int point_pay; // 포인트 결제 금액
  
}
