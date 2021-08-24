package hello.core;

import hello.core.AppConfig;
import hello.core.member.Grade;
import hello.core.member.Member;
import hello.core.member.MemberService;
import hello.core.member.MemberServiceImpl;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

//이렇게 앱 내에서 테스트하는것은 그렇게 좋은 행위는 아니다.
public class MemberApp {
    public static void main(String[] args) {

        // 하나 가입 시켜보자

        //1.appConfig 추가하고 얘가 바뀜
        //MemberService memberService = new MemberServiceImpl();
//      //2.스프링 추가하고 빠짐
//        AppConfig appConfig = new AppConfig();
//        MemberService memberService = appConfig.memberService();
        //3.스프링 버전
        ApplicationContext applicationContext = new AnnotationConfigApplicationContext(AppConfig.class);
        MemberService memberService = applicationContext.getBean("memberService", MemberService.class);


        Member member = new Member(1L, "memberA", Grade.VIP);
        memberService.join(member);

        // 가입 되었나 확인
        Member findMember = memberService.findMember(1L);
        System.out.println("new member = " + member.getName());
        System.out.println("find member = " + findMember.getName());
    }
}
