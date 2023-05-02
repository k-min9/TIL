package com.example.show.mapper;

import java.util.List;

import org.apache.ibatis.annotations.Param;

import com.example.show.dto.ShowDetailDto;
import com.example.show.dto.ShowDto;

public interface ShowMapper {
  
  ShowDto getShowData(@Param("user_no")String user_no, @Param("start_dt")String start_dt);

  List<ShowDetailDto> getShowList(@Param("user_no")String user_no, @Param("start_dt")String start_dt);

}
