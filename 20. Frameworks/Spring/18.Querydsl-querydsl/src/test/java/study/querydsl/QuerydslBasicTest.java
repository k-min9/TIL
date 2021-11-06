package study.querydsl;

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

import static org.assertj.core.api.Assertions.*;

@SpringBootTest
@Transactional
public class QuerydslBasicTest {

    @Autowired
    EntityManager em;

    //테스트용 데이터 세팅
    @BeforeEach
    public void before() {
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
        JPAQueryFactory queryFactory = new JPAQueryFactory(em);  //이것도 em처럼 필드로 빼도 괜찮음!, 동시성 문제 같은거 고민 안해도 됨(스프링 주입은 멀티스레드 대응 되어있음)
        // 2. Gradle>Tasks>other>compileQuerydsl 하고 오세요!
        // build > generated에서 관련 Q 타입 확인하여 무사 작동여부 확인 가능

        // 3. Q 타입 사용 (알기 쉽게 일단 이렇게 썼고, 다른 문법도 있음)
        QMember m = new QMember("m"); // Qmember의 인자 "m" : 구분할 이름

        // 작성
        Member findMember = queryFactory
                .select(m)
                .from(m)
                .where(m.username.eq("member1"))
                .fetchOne();

        assertThat(findMember.getUsername()).isEqualTo("member1");


    }

}
