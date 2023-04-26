package com.example.show.entity;

import java.util.ArrayList;
import java.util.List;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.Table;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity
@Table(name = "t_user")
@Getter @Setter @NoArgsConstructor
public class User {
  
  @Id @Column(name = "user_no")
  String userNo;

  String name;

  // 연결
  @OneToMany(mappedBy = "user")
  List<Show> shows = new ArrayList<>();

}
