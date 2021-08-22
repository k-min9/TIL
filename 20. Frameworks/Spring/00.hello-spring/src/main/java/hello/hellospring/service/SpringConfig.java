package hello.hellospring.service;

import hello.hellospring.aop.TimeTraceAop;
import hello.hellospring.repository.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import javax.persistence.EntityManager;
import javax.sql.DataSource;

@Configuration
public class SpringConfig {

    //jdbc와 jdbcTemplate을 위한 구현
//    private DataSource dataSource;
//
//    @Autowired
//    public SpringConfig(DataSource dataSource) {
//        this.dataSource = dataSource;
//    }

    //jpa를 위한 구현
//    private EntityManager em;
//
//    @Autowired
//    public SpringConfig(EntityManager em) {
//        this.em = em;
//    }

//    @Bean
//    public MemberService memberService(){
//        return new MemberService(memberRepository());
//    }

//    @Bean
//    public MemberRepository memberRepository(){
    //1.기존의 자바 메모리
    //return new MemoryMemberRepository();
    //2.기존의 DB를 갈아끼기만 해도 이게 작동한다. SOLID의 OCP:개방-폐쇄 원칙을 스프링의 DI를 통해 훌륭히 구현
    //return new JdbcMemberRepository(dataSource);
    //3.jdbc Template로 구현 (테스트 환경은 동일)
    //return new JdbcTemplateMemberRepository(dataSource);
    //4. JPA로 구현
    //return new JpaMemberRepository(em);
    //}

    //스프링 데이터 jpa를 위한 구현
    private final MemberRepository memberRepository;

    @Autowired
    public SpringConfig(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

    //5. 스프링 데이터 JPA로 구현
    @Bean
    public MemberService memberService(){
        return new MemberService(memberRepository);
    }

    //AOP 사용을 명시하기에는 컴퍼넌트 스캔 안쓰는 쪽이 좋다.
//    @Bean
//    public TimeTraceAop timeTraceAop(){
//        return new TimeTraceAop();
//    }
}
