package study.querydsl;

import com.querydsl.core.QueryResults;
import com.querydsl.core.Tuple;
import com.querydsl.jpa.impl.JPAQueryFactory;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.transaction.annotation.Transactional;
import study.querydsl.entity.Member;
import study.querydsl.entity.QMember;
import study.querydsl.entity.QTeam;
import study.querydsl.entity.Team;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.PersistenceUnit;

import java.util.List;

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


    /** 페치 조인 : 아무리 강조해도 지나침이 없는 */
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


}
