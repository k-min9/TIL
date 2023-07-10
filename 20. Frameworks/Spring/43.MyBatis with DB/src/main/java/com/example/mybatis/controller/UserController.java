package com.example.mybatis.controller;

import com.example.mybatis.dto.PayMethodDto;
import com.example.mybatis.dto.UseDataDto;
import com.example.mybatis.dto.UseListDto;
import com.example.mybatis.dto.UserInfoDto;
import com.example.mybatis.service.UseDataService;
import com.example.mybatis.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.*;

@RestController
@CrossOrigin(origins = "*", allowedHeaders = "*")
@RequestMapping(value = "/api/v1")
@RequiredArgsConstructor
public class UserController {

    private final UserService userService;

    private final UseDataService useDataService;

    @RequestMapping(value = "/user/{user_no}", method = RequestMethod.GET)
    public UserInfoDto getUserInfo(@PathVariable("user_no") String user_no) {
        UserInfoDto result = userService.getUserInfo(user_no);
        return result;
    }

    @RequestMapping(value = "/user/{user_no}/usage/summary", method = RequestMethod.GET)
    public UseDataDto getUseData(@PathVariable("user_no") String user_no, @RequestParam("ptype")int ptype) {
        String start_dt = getStartDt(ptype);

        UseDataDto result = useDataService.getUseData(user_no, start_dt);

        return result;
    }

    @RequestMapping(value = "/user/{user_no}/usage", method = RequestMethod.GET)
    public Map<String, Object>  getUseList(@PathVariable("user_no") String user_no,
                                           @RequestParam(value = "ptype", required = false) Integer ptype) {
        if (ptype == null) ptype = 1;
        String start_dt = getStartDt(ptype);

        Map<String, Object> result = useDataService.getUseList(user_no, start_dt);
        return result;
    }

    @RequestMapping(value = "/user/{user_no}/usage2", method = RequestMethod.GET)
    public Map<String, Object>  getUseList2(@PathVariable("user_no") String user_no,
                                           @RequestParam(value = "ptype", required = false) Integer ptype) {
        if (ptype == null) ptype = 1;
        String start_dt = getStartDt(ptype);

        Map<String, Object> result = useDataService.getUseList2(user_no, start_dt);
        return result;
    }

    @RequestMapping(value = "/pay_methods", method = RequestMethod.GET)
    public List<PayMethodDto> getPayMethod() {
        List<PayMethodDto> result = new ArrayList<>();

        PayMethodDto pm1 = new PayMethodDto();
        pm1.setCode("C");
        pm1.setId("카드2");

        PayMethodDto pm2 = new PayMethodDto();
        pm2.setCode("P");
        pm2.setId("포인트2");

        result.add(pm1);
        result.add(pm2);

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
