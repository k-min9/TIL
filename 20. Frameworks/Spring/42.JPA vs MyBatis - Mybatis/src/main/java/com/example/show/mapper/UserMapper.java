package com.example.show.mapper;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import com.example.show.dto.UserDto;

@Mapper
public interface UserMapper {
  UserDto getUserData(@Param("user_no")String user_no);
}
