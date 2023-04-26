package com.example.show.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.show.entity.User;

public interface UserRepository extends JpaRepository<User, String>{
  User findByUserNo(String user_no); 
}
