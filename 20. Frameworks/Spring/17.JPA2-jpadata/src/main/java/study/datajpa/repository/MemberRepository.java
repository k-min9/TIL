package study.datajpa.repository;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Slice;
import org.springframework.data.jpa.repository.*;
import org.springframework.data.repository.query.Param;
import study.datajpa.dto.MemberDto;
import study.datajpa.entity.Member;

import javax.persistence.QueryHint;
import java.util.Collection;
import java.util.List;
import java.util.Optional;

//@Repository 스프링데이터JPA Repo는 Repository 생략이 가능하다.
public interface MemberRepository extends JpaRepository<Member, Long>, MemberRepositoryCustom {

    /** 1. 스프링 데이터 제공 함수*/

    //스프링 데이터 JPA는 메소드 이름을 분석해서 JPQL을 생성하고 실행
    List<Member> findByUsernameAndAgeGreaterThan(String username, int age);

    //다양한 반환 타입과 페이징 지원
    List<Member> findTop3HelloBy();
    List<Member> findListByUsername(String name); //컬렉션
    Member findMemeberByUsername(String name); //단건
    Optional<Member> findOptionalByUsername(String name); //단건 Optional

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


    /** 페이징 관련 */
    // 특별한 반환 타입 : Page(기존 TotalCount 기능 제공), Slice(11,12,13,14,15,더보기 같은 기능 제공)
    Page<Member> findByAge(int age, Pageable pageable); //count 쿼리 사용
    Slice<Member> findSliceByAge(int age, Pageable pageable); //count 쿼리 사용

    //카운트 쿼리 분리 예시 (성능 최적화, 예시처럼 카운트에는 조인이 필요 없을 수도 있다.)
    @Query(value = "select m from Member m left join m.team t",
            countQuery = "select count(m.username) from Member m")
    Page<Member> findMemberAllCountBy(Pageable pageable);

    // 벌크 쿼리
    @Modifying  // 벌크 쿼리시 발생하는 DB와 영속성 컨텍스트 사이의 괴리를 영속성 컨텍스트 초기화로 없애준다.(em.flush(); em.clear();)
    @Query("update Member m set m.age = m.age + 1 where m.age >= :age")
    int bulkAgePlus(@Param("age") int age);

    // 페치 조인을 스프링 데이터에서 편하게 써보자 >> EntityGraph
    @Override  // findAll 워낙 많이 쓰니까. 이런식으로 오버라이드 할 수 있다는 표기
    @EntityGraph(attributePaths = {"team"})
    List<Member> findAll();

    //쿼리 힌트 (예시 - 나 이거 읽기만 할거니까 더티 체크(변경 감지)같은거 하지 마 라고 말하여 최적화 하는 방식)
    @QueryHints(value = @QueryHint(name = "org.hibernate.readOnly", value = "true"))
    Member findReadOnlyByUsername(String username);

    // projections : 엔티티 대신에 DTO 조회를 편하게(전체 엔티티가 아니라 그 중 이름만 조회하고 싶을때)
    List<UsernameOnly> findProjectionsByUsername(@Param("username") String username);  // 인터페이스 기반
    List<UsernameOnlyDto> findProjectionsDtoByUsername(@Param("username") String username);  // 클래스 기반
    <T> List<T> findProjectionsGenericByUsername(@Param("username") String username, Class<T> type);  // 제네릭 (동적 projection)
    // nested 즉 중첩으로 사용하면 필요한건 제대로 가져오지만 나머지 연관 부분을 엔티티 통째로 가져온다던가 하는 최적화가 안 된 상황을 볼 수 있다
    // 한계를 정리하자면 join 하는 순간 애매해짐

}
