package com.example.mybatis.service;

import com.example.mybatis.dto.UseDataDto;
import com.example.mybatis.dto.UseListDto;
import org.apache.ibatis.annotations.Param;

import java.util.List;
import java.util.Map;

public interface UseDataService {
    UseDataDto getUseData(@Param("user_no")String user_no, @Param("start_dt")String start_dt);

    Map<String, Object> getUseList(@Param("user_no")String user_no, @Param("start_dt")String start_dt);
}
