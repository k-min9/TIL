package study.datajpa.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import study.datajpa.entity.Member;

//@Repository 스프링데이터JPA Repo는 Repository 생략이 가능하다.
public interface MemberRepository extends JpaRepository<Member, Long> {

}
