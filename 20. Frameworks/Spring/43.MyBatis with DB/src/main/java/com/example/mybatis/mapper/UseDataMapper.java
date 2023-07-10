package com.example.mybatis.mapper;

import com.example.mybatis.dto.UseDataDto;
import com.example.mybatis.dto.UseListDto;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface UseDataMapper {
    UseDataDto getUseData(@Param("user_no")String user_no, @Param("start_dt")String start_dt);

    List<UseListDto> getUseList(@Param("user_no")String user_no, @Param("start_dt")String start_dt);
    List<UseListDto> getUseList2(@Param("user_no")String user_no, @Param("start_dt")String start_dt);

    List<UseListDto> getAllUseList();
}
