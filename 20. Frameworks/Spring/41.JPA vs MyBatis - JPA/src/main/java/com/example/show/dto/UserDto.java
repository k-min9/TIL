package com.example.show.dto;

import com.example.show.entity.User;

import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class UserDto {
  private String user_no;
  private String name;

  public UserDto(User user) {
    user_no = user.getUserNo();
    name = user.getName();
  }
}
