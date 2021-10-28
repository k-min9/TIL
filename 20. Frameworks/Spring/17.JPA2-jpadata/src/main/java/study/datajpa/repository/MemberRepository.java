package study.datajpa.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import study.datajpa.dto.MemberDto;
import study.datajpa.entity.Member;

import java.util.List;

//@Repository 스프링데이터JPA Repo는 Repository 생략이 가능하다.
public interface MemberRepository extends JpaRepository<Member, Long> {

    /** 1. 스프링 데이터 제공 함수*/

    //스프링 데이터 JPA는 메소드 이름을 분석해서 JPQL을 생성하고 실행
    List<Member> findByUsernameAndAgeGreaterThan(String username, int age);

    List<Member> findTop3HelloBy();

    /** 2. Query 이용 단순 조회 */

    @Query("select m from Member m where m.username= :username and m.age = :age")
    List<Member> findUser(@Param("username") String username, @Param("age") int age);

    //단순히 값을 하나 조회
    @Query("select m.username from Member m")
    List<String> findUsernameList();

    /** 3. DTO로 직접 조회 */
    // new 필수 + 패키지 적어야 함
    @Query("select new study.datajpa.dto.MemberDto(m.id, m.username, t.name) from Member m join m.team t")
    List<MemberDto> findMemberDto();

    /** 리스트 파라미터 바인딩 예시 */
    @Query("select m from Member m where m.username in :names") // in 절을 이용해서 예쁘게 만들기
    List<Member> findByNames(@Param("names") List<String> names);

}
