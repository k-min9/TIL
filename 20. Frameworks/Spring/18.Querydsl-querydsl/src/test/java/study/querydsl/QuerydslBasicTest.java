package study.querydsl;

import com.querydsl.core.QueryResults;
import com.querydsl.jpa.impl.JPAQueryFactory;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.transaction.annotation.Transactional;
import study.querydsl.entity.Member;
import study.querydsl.entity.QMember;
import study.querydsl.entity.Team;

import javax.persistence.EntityManager;

import java.util.List;

import static org.assertj.core.api.Assertions.*;
import static study.querydsl.entity.QMember.*;

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
}
