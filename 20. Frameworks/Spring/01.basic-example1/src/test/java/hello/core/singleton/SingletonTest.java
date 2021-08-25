package hello.core.singleton;

import hello.core.AppConfig;
import hello.core.member.MemberService;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import static org.assertj.core.api.Assertions.assertThat;

public class SingletonTest {

    @Test
    @DisplayName("스프링 없는 순수한 DI 컨테이너")
    void PureContainer(){
        AppConfig appConfig = new AppConfig();
        //1. 조회 : 호출할때마다 객체 생성
        MemberService memberService1 = appConfig.memberService();

        //2. 조회 : 호출할때마다 객체 생성
        MemberService memberService2 = appConfig.memberService();

        //참조값 다른지 확인
        System.out.println("memServ1" + memberService1);
        System.out.println("memServ2" + memberService2);

        //다른지 확인 2
        assertThat(memberService1).isNotSameAs(memberService2);
    }

    @Test
    @DisplayName("싱글톤 패턴을 적용한 객체 사용용")
    void singletonServiceTest(){
        SingletonService singletonService1 = SingletonService.getInstance();
        SingletonService singletonService2 = SingletonService.getInstance();

        System.out.println("1 = " + singletonService1);
        System.out.println("2 = " + singletonService2);

        assertThat(singletonService1).isSameAs(singletonService2);
    }

    @Test
    @DisplayName("스프링 컨테이너와 싱글통")
    void SpringContainer(){
        ApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);
        //1. 조회
        MemberService memberService1 = ac.getBean("memberService", MemberService.class);
        MemberService memberService2 = ac.getBean("memberService", MemberService.class);

        //참조값 다른지 확인
        System.out.println("memServ1" + memberService1);
        System.out.println("memServ2" + memberService2);

        //다른지 확인 2
        assertThat(memberService1).isSameAs(memberService2);
    }
}
