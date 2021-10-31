package study.datajpa.repository;

import study.datajpa.entity.Member;

import java.util.List;

// 사용자 정의 리포지토리 구현용 인터페이스(이름 자유롭게)
public interface MemberRepositoryCustom {
    List<Member> findMemberCustom();
}
