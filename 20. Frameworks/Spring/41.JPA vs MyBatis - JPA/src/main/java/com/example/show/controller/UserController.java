package com.example.show.controller;

import java.util.Calendar;
import java.util.Map;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.example.show.dto.ShowDto;
import com.example.show.service.ShowService;

import lombok.RequiredArgsConstructor;

@RestController
@CrossOrigin(origins = "*", allowedHeaders = "*")
@RequestMapping(value = "/api/v1")
@RequiredArgsConstructor
public class UserController {

  private final ShowService showService;

  // 요약된 내용을 반환
  @RequestMapping(value = "/user/{user_no}/usage/summary", method = RequestMethod.GET)
  public ShowDto getShowData(@PathVariable("user_no") String user_no, @RequestParam("ptype")int ptype) {
    String start_dt = getStartDt(ptype);

    ShowDto result = showService.getShowData(user_no, start_dt);
    return result;
  }

  /**
   * List로 공연목록 및 사용 금액
   * @param type
   * @return
   */
  @GetMapping("/user/{user_no}/usage")
  public Map<String, Object> getShowList(@PathVariable("user_no") String user_no, @RequestParam("ptype")int ptype) {
    String start_dt = getStartDt(ptype);

    Map<String, Object> result = showService.getShowList(user_no, start_dt);
    return result;
  }

  // start dt 계산
  private String getStartDt(int type) {
    Calendar cur = Calendar.getInstance();
    
    switch (type) {
      case 1: // 1주일 전
        cur.add(Calendar.DATE, -7);
        break;
      case 2: // 1달 전
        cur.add(Calendar.MONTH, -1);
        break;
      case 3: // 1년 전
        cur.add(Calendar.YEAR, -1);
        break;
      default:
        cur.add(Calendar.DATE, -7);
        break;
    }

    String startDt = new java.text.SimpleDateFormat("yyyy-MM-dd").format(cur.getTime());
    return startDt;
  }
}