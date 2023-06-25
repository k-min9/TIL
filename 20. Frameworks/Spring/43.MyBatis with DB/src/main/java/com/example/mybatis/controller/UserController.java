package com.example.mybatis.controller;

import com.example.mybatis.dto.UseDataDto;
import com.example.mybatis.dto.UseListDto;
import com.example.mybatis.dto.UserInfoDto;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.*;

@RestController
@CrossOrigin(origins = "*", allowCredentials = "*")
@RequestMapping(value = "/api/v1")
@RequiredArgsConstructor
public class UserController {

    @RequestMapping(value = "/user/{user_no}", method = RequestMethod.GET)
    public UserInfoDto getUserInfo(@PathVariable("user_no") String user_no) {
        UserInfoDto result = new UserInfoDto();
        result.setUser_no("ME0001");
        result.setName("강민구");
        return result;
    }

    @RequestMapping(value = "/user/{user_no}/usage/summary", method = RequestMethod.GET)
    public UseDataDto getUseData(@PathVariable("user_no") String user_no, @RequestParam("ptype")int ptype) {
        String start_dt = getStartDt(ptype);
        UseDataDto result = new UseDataDto();

        result.setUsage_count(3);
        result.setUsage_meter(234);
        result.setUsage_minute(30);
        result.setCarbon_reduction(1.23f);

        return result;
    }

    @RequestMapping(value = "/user/{user_no}/usage", method = RequestMethod.GET)
    public Map<String, Object>  getUseList(@PathVariable("user_no") String user_no, @RequestParam("ptype")int ptype) {
        String start_dt = getStartDt(ptype);

        Map<String, Object> result = new HashMap<>();
        List useList = new ArrayList();
        UseListDto useListDto1 = new UseListDto();
        useListDto1.setUse_no("no.1");
        useList.add(useListDto1);
        UseListDto useListDto2 = new UseListDto();
        useListDto2.setUse_no("no.2");
        useList.add(useListDto2);
        UseListDto useListDto3 = new UseListDto();
        useListDto3.setUse_no("no.3");
        useList.add(useListDto3);
        result.put("list", useList);

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
