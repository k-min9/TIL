package com.example.show.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import com.example.show.entity.Show;

public interface ShowRepository extends JpaRepository<Show, String> {

  // 특정 인물이 특정 날짜 이래로 본 쇼 전부
  @Query("select s from Show join fetch s.user su where su.userNo = :userNo and s.startDt >= :startDt")
  List<Show> findShowCustom(@Param("userNo") String userNo, @Param("startDt") String startDt);

  // 특정 인물이 특정 날짜 이래로 본 쇼와 결제 금액 전부
  @Query("select s from Show join fetch s.pays su where s.user.userNo = :userNo and s.startDt >= :startDt order by s.startDt")
  List<Show> findShowJoinPay(@Param("userNo") String userNo, @Param("startDt") String startDt);

}
