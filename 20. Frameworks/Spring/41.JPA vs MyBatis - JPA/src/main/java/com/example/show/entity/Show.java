package com.example.show.entity;

import java.util.List;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.OneToMany;
import javax.persistence.Table;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity
@Table(name = "t_show")
@Getter @Setter @NoArgsConstructor
public class Show {

  @Id @Column(name = "SHOW_NO")
  String showNo;

  // @Column(name = "USER_NO")  // FK
  // String userNo;

  @Column(name = "MACHINE_NO")
  String machineNo;

  @Column(name = "charge_no")
  String chageNo;

  @Column(name = "strt_dt")
  String startDt;

  @Column(name = "end_dt")
  String endDt;

  @Column(name = "show_time")
  int showTime;

  @Column(name = "show_charge")
  int showCharge;

  // 연결
  @ManyToOne(fetch = FetchType.LAZY)
  @JoinColumn(name = "USER_NO")  // FK 이름
  User user;

  @OneToMany(mappedBy = "show")
  List<Showpay> showpays;

}
