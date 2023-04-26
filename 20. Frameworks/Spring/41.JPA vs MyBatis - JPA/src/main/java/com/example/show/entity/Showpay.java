package com.example.show.entity;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity
@Table(name = "t_pay")
@Getter @Setter @NoArgsConstructor
public class Showpay {
  
  @Id @Column(name = "pay_no")
  String payNo;

  String payDt;

  String payCost;

  String payMethodCd;

  // 연결
  @ManyToOne(fetch = FetchType.LAZY)
  @JoinColumn(name = "show_no")
  Show show;
}
