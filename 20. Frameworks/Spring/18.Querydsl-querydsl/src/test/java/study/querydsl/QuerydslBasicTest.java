package study.querydsl;

import com.querydsl.core.QueryResults;
import com.querydsl.core.Tuple;
import com.querydsl.core.types.Expression;
import com.querydsl.core.types.Projections;
import com.querydsl.core.types.dsl.CaseBuilder;
import com.querydsl.core.types.dsl.Expressions;
import com.querydsl.core.types.dsl.NumberExpression;
import com.querydsl.jpa.JPAExpressions;
import com.querydsl.jpa.impl.JPAQueryFactory;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.transaction.annotation.Transactional;
import study.querydsl.dto.MemberDto;
import study.querydsl.entity.Member;
import study.querydsl.entity.QMember;
import study.querydsl.entity.QTeam;
import study.querydsl.entity.Team;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.PersistenceUnit;

import java.util.List;

import static com.querydsl.jpa.JPAExpressions.*;
import static org.assertj.core.api.Assertions.*;
import static study.querydsl.entity.QMember.*;
import static study.querydsl.entity.QTeam.*;

@SpringBootTest
@Transactional
public class QuerydslBasicTest {

    @Autowired
    EntityManager em;

    JPAQueryFactory queryFactory;

    //테스트용 데이터 세팅
    @BeforeEach
    public void before() {
        queryFactory = new JPAQueryFactory(em);  // 동시성 문제 없음 + 멀티스레드 대응
        Team teamA = new Team("teamA");
        Team teamB = new Team("teamB");
        em.persist(teamA);
        em.persist(teamB);

        Member member1 = new Member("member1", 10, teamA);
        Member member2 = new Member("member2", 20, teamA);
        Member member3 = new Member("member3", 30, teamB);
        Member member4 = new Member("member4", 40, teamB);
        em.persist(member1);
        em.persist(member2);
        em.persist(member3);
        em.persist(member4);
    }

    @Test
    public void startJPQL() {
        //member1을 찾아라.
        String qlString =
                "select m from Member m " +
                "where m.username = :username";
        Member findMember = em.createQuery(qlString, Member.class)
                .setParameter("username", "member1")
                .getSingleResult();

        assertThat(findMember.getUsername()).isEqualTo("member1");
    }

    /** 기본적인 Querydsl 사용법*/
    @Test
    public void startQuerydsl() {
        // 1. JPAQueryFactory 필요함 (Enitity Manager 등록으로 확인)
        JPAQueryFactory queryFactory2 = new JPAQueryFactory(em);  //이것도 em처럼 필드로 빼도 괜찮음!, 동시성 문제 같은거 고민 안해도 됨(스프링 주입은 멀티스레드 대응 되어있음)
        // 2. Gradle>Tasks>other>compileQuerydsl 하고 오세요!
        // build > generated에서 관련 Q 타입 확인하여 무사 작동여부 확인 가능

        // 3. Q 타입 사용 (알기 쉽게 일단 이렇게 썼고, 다른 문법도 있음)
        QMember m = new QMember("m"); // Qmember의 인자 "m" : 구분할 이름
        // 다른 문법 : QMember m = QMember.member;  // 이걸 static import 해서 그냥 member만 밑에 바로 써버리는 방법도 있고...

        // 작성
        Member findMember = queryFactory2
                .select(m)
                .from(m)
                .where(m.username.eq("member1"))
                .fetchOne();

        assertThat(findMember.getUsername()).isEqualTo("member1");


    }

    @Test
    public void search() {
        Member findMember = queryFactory
                .selectFrom(member)  // select와 from을 합치고, QMember.member을 member로 static import해서 그대로 사용
                .where(member.username.eq("member1")  // 이름이 member1이면서
                        .and(member.age.between(10, 30)))  // 나이가 10살~ 30살인 사람을 조회해
                .fetchOne();

        assertThat(findMember.getUsername()).isEqualTo("member1");

        // and 두번째 방법 (위 체이닝보다 깔끔하다)
        Member findMember2 = queryFactory
                .selectFrom(member)  // select와 from을 합치고, QMember.member을 member로 static import해서 그대로 사용
                .where(member.username.eq("member2"),  // 이름이 member2이면서
                       member.age.between(10, 30))  // 나이가 10살~ 30살인 사람을 조회해
                .fetchOne();
        assertThat(findMember2.getUsername()).isEqualTo("member2");
    }

    @Test
    public void resultFetch() {
        // 둘 이상의 결과를 리스트로 반환
        List<Member> fetchList = queryFactory
                .selectFrom(member)
                .fetch();

//        // 단 건 조회 (없으면 null 있으면 notunique~exception)
//        Member fetchOne = queryFactory
//                .selectFrom(QMember.member)
//                .fetchOne();

        // limit(1).fetchOne()
        Member fetchFirst = queryFactory
                .selectFrom(QMember.member)
                .fetchFirst();

        // 페이징 정보 포함 (토탈 카운트도 실행)
        QueryResults<Member> results = queryFactory
                .selectFrom(member)
                .fetchResults();
        results.getTotal();
        List<Member> content = results.getResults();

        // 카운트 용 쿼리로 바꿔서 그것만 실행
        long total = queryFactory
                .selectFrom(member)
                .fetchCount();
    }

    /**
     * 테스트 정렬 설정 순서
     * 1. 회원 나이 내림차순(desc)
     * 2. 회원 이름 올림차순(asc)
     * 3. 회원 이름 없을 경우 마지막에 출력(nulls last)
     * */
    @Test
    public void sort() {
        // 정렬용 초기화
        em.persist(new Member(null, 100));
        em.persist(new Member("member5", 100));
        em.persist(new Member("member6", 100));

        List<Member> results = queryFactory
                .selectFrom(member)
                .where(member.age.eq(100))
                .orderBy(member.age.desc(), member.username.asc().nullsLast())
                .fetch();

        for (Member result : results) {
            System.out.println("이름 = " + result.getUsername());
        }
        // 5 > 6 > null 순으로 정렬되는것을 볼 수 있다.
    }

    @Test
    public void paging() {
        List<Member> results = queryFactory
                .selectFrom(member)
                .orderBy(member.username.desc())
                .offset(1)
                .limit(2)
                .fetch();

        for (Member result : results) {
            System.out.println("result = " + result);
        }
    }

    @Test
    public void paging2() {
        QueryResults<Member> results = queryFactory
                .selectFrom(member)
                .orderBy(member.username.desc())
                .offset(1)
                .limit(2)
                .fetchResults();

        assertThat(results.getTotal()).isEqualTo(4);
        assertThat(results.getLimit()).isEqualTo(2);
        assertThat(results.getOffset()).isEqualTo(1);
        assertThat(results.getResults().size()).isEqualTo(2);

        // 이렇게 단순하면 상관 없는데, 컨텐츠 쿼리는 복잡하지만 카운트 쿼리는 간단할때는 따로짜는게 더 좋을때도 있다.
        // ex) where을 붙이면 양쪽 쿼리, 모든 조인에 다 붙는데, 그게 카운트에는 필요 없을때가 있다.
    }

    @Test
    public void aggregation() {
        // 여러 가지 반환 타입에 대응하기 위해서 querydsl은 튜플 타입을 제공함
        List<Tuple> results = queryFactory
                .select(
                        member.count(),
                        member.age.sum(),
                        member.age.avg(),
                        member.age.max(),
                        member.age.min()
                )
                .from(member)
                .fetch();

        // 10, 20, 30, 40 일테니까
        Tuple tuple = results.get(0);
        assertThat(tuple.get(member.count())).isEqualTo(4);
        assertThat(tuple.get(member.age.sum())).isEqualTo(100);
        assertThat(tuple.get(member.age.avg())).isEqualTo(25);
        assertThat(tuple.get(member.age.max())).isEqualTo(40);
        assertThat(tuple.get(member.age.min())).isEqualTo(10);

    }

    /**팀의 이름과 각 팀의 평균 연령을 구해보자*/
    @Test
    public void groupBy() throws Exception {
        List<Tuple> results = queryFactory
                .select(team.name, member.age.avg())
                .from(member)
                .join(member.team, team)
                .groupBy(team.name)
                .fetch();

        Tuple teamA = results.get(0);  // 10, 20
        Tuple teamB = results.get(1);  // 30, 40

        assertThat(teamA.get(team.name)).isEqualTo("teamA");
        assertThat(teamA.get(member.age.avg())).isEqualTo(15);

        assertThat(teamB.get(team.name)).isEqualTo("teamB");
        assertThat(teamB.get(member.age.avg())).isEqualTo(35);
    }

    @Test
    public void join() {
        List<Member> results = queryFactory
                .selectFrom(member)
                // left join, inner join, theta join(연관관계가 없는 대상간의 조인) 가능
                .join(member.team, team)  // 조인대상, 별칭(alias) : member.team as team
                .where(team.name.eq("teamA"))
                .fetch();

        assertThat(results)
                .extracting("username")  // assertJ 지원 함수, extract(추출)하고, 검증한다. 여러필드 한번에 추출 검증에 유용
                .containsExactly("member1", "member2");
    }


    /** 세타(크로스) 조인(막조인...) 예시 : 회원의 이름이 팀 이름과 같은 회원 조회 : 연관성 없는 관계 대상 간 조인 */
    @Test
    public void theta_join() {
        em.persist(new Member("teamA"));
        em.persist(new Member("teamB"));

        List<Member> results = queryFactory
                .select(member)
                .from(member, team)
                .where(member.username.eq(team.name))
                .fetch();

        for (Member result : results) {
            System.out.println("result = " + result);
        }
    }

    /**
     * 팀 이름이 teamA인 팀만 조인, 회원은 모두 조회
     * JPQL에서는 "select m, t from Member m left join m.team t on t.name = 'teamA'"
     * */
    @Test
    public void join_on_filtering() {
        List<Tuple> results = queryFactory
                .select(member, team)
                .from(member)
                .leftJoin(member.team, team)
                .on(team.name.eq("teamA"))
                .fetch();

        // leftjoin이니까 member는 다 긁어오는데 team 이름이 teamA인 team만 가져는걸 확인할 수 있다.
        // 그냥 join하면 inner 하면서 member3, member4는 아예 빠짐... 뭐 이렇게 쓸거면 그냥 on 안쓰고 where로 결과 필터링 해도 되니까 의미가 적다
        for (Tuple result : results) {
            System.out.println("result = " + result);
        }
    }

    /** 막 조인 예시 : 잘보면 join이 member.team이 아니라 진짜 그냥 team을 박았다. 세타조인과 마찬가지로 cross join됨 */
    @Test
    public void join_on_like_theta_join() {
        em.persist(new Member("teamA"));
        em.persist(new Member("teamB"));
        em.persist(new Member("teamC"));

        List<Tuple> results = queryFactory
                .select(member, team)
                .from(member)
                .leftJoin(team)  // 아이디 매칭 없이 그냥 관계 없는 두 대상도 막 조인 (left outer join 쿼리 확인 가능)
                .on(member.username.eq(team.name))
                .fetch();

        for (Tuple result : results) {
            System.out.println("result = " + result);
        }
    }


    /** 페치 조인 : 아무리 강조해도 지나침이 없는
     * 페치조인 대상에 on이나 where로 필터링시, DB의 상태와 객체의 상태간 일관성이 깨진다. */
    @PersistenceUnit
    EntityManagerFactory emf;  // 페치조인이 무사히 LAZY 설정된 team을 가져왔나 확인 하기 위해서

    @Test
    public void fetchJoin() {
        em.flush();
        em.clear();

        Member findMember = queryFactory
                .selectFrom(member)
                .join(member.team, team).fetchJoin()  // .fetchJoin() 이것만 붙이면 알아서 페치조인 처리를 해줌
                .where(member.username.eq("member1"))
                .fetchOne();

        boolean loaded = emf.getPersistenceUnitUtil().isLoaded(findMember.getTeam());  // team이 영속성 컨텍스트에 로드돠었는지 여부
        assertThat(loaded).as("페치 조인 미적용!").isTrue();
    }


    /** 서브쿼리 예제 1 : 나이가 가장 많은 사람 하나 뽑아 볼까*/
    @Test
    public void subQuery() {
        // alias가 중복되면 안되니까 QMember 인스턴스 하나 따로 만들어준다.
        QMember memberSub = new QMember("memberSub");

        List<Member> results = queryFactory
                .selectFrom(member)
                .where(member.age.eq(
                        // 서브 쿼리 내 새 alias 선언, 안하면 충돌나니까
                        select(memberSub.age.max())
                                .from(memberSub)
                ))
                .fetch();
        
        assertThat(results).extracting("age").containsExactly(40);
    }

    /** 서브쿼리 예제 2: 10살 넘는 사람*/
    @Test
    public void subQuerywithIn() {
        // alias가 중복되면 안되니까 QMember 인스턴스 하나 따로 만들어준다.
        QMember memberSub = new QMember("memberSub");

        List<Member> results = queryFactory
                .selectFrom(member)
                .where(member.age.in(
                        // 서브 쿼리 내 새 alias 선언, 안하면 충돌나니까
                        select(memberSub.age)
                                .from(memberSub)
                                .where(memberSub.age.gt(10))  // 20, 30, 40 이 서브쿼리로 나옴
                ))
                .fetch();

        assertThat(results).extracting("age").containsExactly(20, 30, 40);
    }

    /** 서브쿼리 예제 3 : 셀렉트에 서브쿼리 넣기 + JPAExpressions.select를 static import (예제 1, 2까지 다 되 버렸네...) */
    @Test
    public void selectSubQuery() {
        QMember memberSub = new QMember("memberSub");

        List<Tuple> results = queryFactory
                .select(member.username,
                        select(memberSub.age.avg())
                                .from(memberSub))
                .from(member)
                .fetch();

        for (Tuple result : results) {
            System.out.println("result = " + result);
        }
    }

    /** JPQL, querydsl의 한계 : From절의 서브쿼리는 지원하지 않는다. 원래는 select 절도 안되는데, 하이버네이트에서 지원해주는 것을 querydsl에서 사용하고 있다.
     * 해결법 : 서브 쿼리가 아니라 join으로 해결한다(할 수 있으면), 쿼리를 2번 분리해서 실행한다, NATIVE SQL을 사용한다. */


    // CASE문 : 조건에 따라 값 정하기 (90~100점은 A 80~90점은 B...)
    // 이런 것은 DB에서 처리할게 아니라 가져와서 비지니스 로직 차원에서 정리하는 것이 좋다
    // 1. 단순 버전
    @Test
    public void case_simple() {
        List<String> result = queryFactory
                .select(member.age
                        .when(10).then("10살")
                        .when(20).then("20살")
                        .otherwise("기타"))
                .from(member)
                .fetch();

        for (String s : result) {
            System.out.println("s = " + s);
        }
    }

    // 2. 복잡 버전
    @Test
    public void case_complex() {
        List<String> result = queryFactory
                .select(new CaseBuilder()
                        .when(member.age.between(0, 20)).then("0~20살")
                        .when(member.age.between(21, 30)).then("21~30살")
                        .otherwise("기타"))
                .from(member)
                .fetch();

        for (String s : result) {
            System.out.println("s = " + s);
        }
    }

    // orderBy와 case 조합해서 원하는 순서대로 회원 출력
    @Test
    public void case_with_orderBy() {
        // 조건(30살 초과~, 0~20살, 21~30살 순서대로 출력)을 변수로 선언해버린다.
        NumberExpression<Integer> rankPath = new CaseBuilder()
                .when(member.age.between(0, 20)).then(2)
                .when(member.age.between(21, 30)).then(1)
                .otherwise(3);

        // 변수화 한 조건을 사용할 수 있는게 바로 querydsl의 장점
        List<Tuple> result = queryFactory
                .select(member.username, member.age, rankPath)
                .from(member)
                .orderBy(rankPath.desc())  // 등록한 rank를 이용하여 정렬한다.
                .fetch();

        for (Tuple tuple : result) {
            String username = tuple.get(member.username);
            Integer age = tuple.get(member.age);
            Integer rank = tuple.get(rankPath);
            System.out.println("username = " + username + " age = " + age + " rank = " + rank);
        }
    }


    /** 결과물에 상수나 문자 더하기 */
    // 상수 : Expressions.constant("더할 상수")
    @Test
    public void constant() {
        List<Tuple> results = queryFactory
                .select(member.username, Expressions.constant("A"))
                .from(member)
                .fetch();

        for (Tuple result : results) {
            System.out.println("result = " + result); // [member1, A], [member2, A], [member3, A], [member4, A] 출력
        }
    }

    // 문자 (username_age 식으로 써보자)
    @Test
    public void concat() {
        List<String> results = queryFactory
                .select(member.username
                        .concat("_")
                        .concat(member.age.stringValue()))  // stringValue : 숫자를 문자로 변환 (잊지 말자!), 앞으로 Enum 처리할 일 생기면 심심찮게 쓰는 함수
                .from(member)
                //.where(member.username.eq("member1"))
                .fetch();

        for (String result : results) {
            System.out.println("result = " + result);
        }
        // 출력값
        // result = member1_10
        // result = member2_20
        // result = member3_30
        // result = member4_40
    }

    /** DTO 조회
     * JPQL 문법 :  em.createQuery("select new study.querydsl.dto.MemberDto(m.username, m.age) from Member m", MemberDto.class)
     * new를 이용한 생성자방법만 지원하고, 패키지 이름을 일일히 적어줘야 해서 매우 지저분함
     * querydsl은 세가지 방법 지원 : 프로퍼티 접근, 필드 직접 접근, 생성자 사용
     * */

    // 1. 프로퍼티 접근
    @Test
    public void findDtoBySetter() {
        List<MemberDto> results = queryFactory
                .select(Projections.bean(MemberDto.class,
                        member.username,
                        member.age))
                .from(member)
                .fetch();

        for (MemberDto result : results) {
            System.out.println("result = " + result);
        }
    }

    // 2. 필드 접근 (Getter, Setter 필요 없이 그냥 값을 박아버린다.)
    // 그러니까 이름 맞춰줘야 한다. DTO와 이름이 안 맞을 경우, member.username.as("name") 이런식으로 가능 ; name이 DTO쪽 필드이름)
    @Test
    public void findDtoByField() {
        List<MemberDto> results = queryFactory
                .select(Projections.fields(MemberDto.class,
                        member.username,
                        member.age))
                .from(member)
                .fetch();

        for (MemberDto result : results) {
            System.out.println("result = " + result);
        }
    }

    // 3. 생성자 접근 (타입을 맞춰줘야 한다.)
    @Test
    public void findDtoByConstructor() {
        List<MemberDto> results = queryFactory
                .select(Projections.constructor(MemberDto.class,
                        member.username,
                        member.age))
                .from(member)
                .fetch();

        for (MemberDto result : results) {
            System.out.println("result = " + result);
        }
    }
}
