package com.example.show.service;

import java.util.List;

import org.springframework.stereotype.Service;

import com.example.show.dto.ShowDto;
import com.example.show.entity.Show;
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

}
