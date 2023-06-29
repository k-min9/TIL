package com.example.mybatis.service;

import com.example.mybatis.dto.UserInfoDto;
import com.example.mybatis.mapper.UserMapper;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class UserServiceImpl implements UserService {

    private final UserMapper userMapper;


    @Override
    public UserInfoDto getUserInfo(String user_no) {
        UserInfoDto result = userMapper.getUserInfo(user_no);

        return result;
    }
}
