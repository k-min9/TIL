package com.example.show.service;

import org.springframework.stereotype.Service;

import com.example.show.dto.UserDto;
import com.example.show.mapper.UserMapper;

import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class UserService {
  
  private final UserMapper userMapper;

  public UserDto getUserData(String user_no) {
    UserDto result = userMapper.getUserData(user_no);

    return result;
  }

}
