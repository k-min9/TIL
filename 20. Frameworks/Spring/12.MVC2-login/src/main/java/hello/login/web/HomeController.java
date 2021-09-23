package hello.login.web;

import hello.login.domain.member.Member;
import hello.login.domain.member.MemberRepository;
import hello.login.web.argumentresolver.Login;
import hello.login.web.session.SessionConst;
import hello.login.web.session.SessionManager;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.CookieValue;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.SessionAttribute;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

@Slf4j
@Controller
@RequiredArgsConstructor
public class HomeController {

    private final MemberRepository memberRepository;
    private final SessionManager sessionManager;

    //로그인 안해도 들어오게 required false
//    @GetMapping("/")
//    public String homeLogin(@CookieValue(name = "memberId", required = false) Long memberId, Model model){
//
//        //로그인 안한 사용자
//        if (memberId == null){
//            return "home";
//        }
//
//        //로그인
//        Member loginMember = memberRepository.findById(memberId);
//        if (memberId == null){
//            return "home";
//        }
//
//        model.addAttribute("member", loginMember);
//        return "loginHome";
//    }

    // 직접 만든 세션 사용
//    @GetMapping("/")
//    public String homeLoginV2(HttpServletRequest request, Model model){
//
//        //세션 관리자에 저장된 회원 정보
//        Member member = (Member)sessionManager.getSession(request);
//
//        if (member == null){
//            return "home";
//        }
//
//        model.addAttribute("member", member);
//        return "loginHome";
//    }

    //@GetMapping("/")
    public String homeLoginV2(HttpServletRequest request, Model model){

        //로그인 하지 않고 처음 접속한 사람도 세션이 만들어지는 것 방지
        HttpSession session = request.getSession(false);
        if (session == null) {
            return "home";
        }

        Member loginMember = (Member)session.getAttribute(SessionConst.LOGIN_MEMBER);

        //세션 정보 없음
        if (loginMember == null){
            return "home";
        }

        //세션 정보 있음 = 로그인
        model.addAttribute("member", loginMember);
        return "loginHome";
    }

    //V2의 스프링 어노테이션 버전이라는데 글쎄... 딱히 편해진거 같진 않은데;;
//    @GetMapping("/")
//    public String homeLoginV3(
//            @SessionAttribute(name = SessionConst.LOGIN_MEMBER, required = false) Member loginMember, Model model) {
//
//        //세션에 회원 데이터가 없으면 home
//        if (loginMember == null) {
//            return "home";
//        }
//
//        //세션이 유지되면 로그인으로 이동
//        model.addAttribute("member", loginMember);
//        return "loginHome";
//    }

    @GetMapping("/")
    public String homeLoginV3ArgumentResolver(@Login Member loginMember, Model model) {

        //세션에 회원 데이터가 없으면 home
        if (loginMember == null) {
            return "home";
        }

        //세션이 유지되면 로그인으로 이동
        model.addAttribute("member", loginMember);
        return "loginHome";
    }

}