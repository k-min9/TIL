package com.example.mybatis.controller;

import com.example.mybatis.dto.UserInfoDto;
import com.example.mybatis.service.UseDataService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@CrossOrigin(origins = "*", allowedHeaders = "*")
@RequestMapping(value = "/api/v1")
@RequiredArgsConstructor
public class UseController {

    private final UseDataService useDataService;

    @RequestMapping(value = "/use", method = RequestMethod.GET)
    public Map<String, Object> getUseListByPaymethodName(@RequestParam(value = "paymethod", required = false) String paymethod) {
        Map<String, Object> result = useDataService.getUseListByPaymethodName(paymethod);
        return result;
    }

}
