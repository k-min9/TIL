package com.example.show.service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Service;

import com.example.show.dto.ShowDetailDto;
import com.example.show.dto.ShowDto;
import com.example.show.entity.Show;
import com.example.show.entity.Showpay;
import com.example.show.repository.ShowRepository;

import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class ShowService {
  
  private final ShowRepository showRepository;

  // 요약 내용
  public ShowDto getShowData(String use_no, String start_dt) {
    ShowDto result = new ShowDto();

    List<Show> shows = showRepository.findShowCustom(use_no, start_dt);
    for (Show show: shows) {
      result.setShow_count(result.getShow_count()+1);
      result.setShow_charge(result.getShow_charge()+show.getShowCharge());
      result.setShow_time(result.getShow_time()+show.getShowTime());
    }

    float chargeReduction = (float)(result.getShow_charge()*0.2/20);
    chargeReduction = Math.round(chargeReduction*10)/10;  // 소수 1자리 반올림 예시
    result.setCharge_reduction(chargeReduction);
    // 반올림 필요하면 

    return result;
  }


  private Map<String, Object> getShowList(String user_no, String start_dt) {
    Map<String, Object> result = new HashMap<>();
    List<ShowDetailDto> dtos = new ArrayList<>();

    List<Show> shows = showRepository.findShowJoinPay(user_no, start_dt);
    for (Show show : shows) {
      ShowDetailDto dto = new ShowDetailDto();
      dto.setShow_no(show.getShowNo());
      dto.setShow_time(show.getShowTime());
      dto.setShow_start_dt(show.getStartDt());
      dto.setShow_end_dt(show.getEndDt());
      for (Showpay showpay: show.getShowpays()) {
        dto.setShow_pay_dt(showpay.getPayDt());
        if ("C".equals(showpay.getPayMethodCd())) {
          dto.setCard_pay(dto.getCard_pay()+showpay.getPayCost());
        } else {
          dto.setPoint_pay(dto.getPoint_pay()+showpay.getPayCost());
        }
      }
      dtos.add(dto);
    }
    result.put("list", dtos);

    return result;
  }
}