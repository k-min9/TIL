package hello.servlet.web.springmvc.v3;

import hello.servlet.domain.member.Member;
import hello.servlet.domain.member.MemberRepository;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.List;


//V2 -> V3로 하나씩 바꾸는거 보여줌
@Controller
@RequestMapping("/springmvc/v3/members")
public class SpringMemberControllerV3 {

    private MemberRepository memberRepository = MemberRepository.getInstance();

    //중복부분 주소 제거
    @RequestMapping("/new-form") //GetMapping으로 변경 가능
// V2 버전
//    public ModelAndView newForm() {
//        return new ModelAndView("new-form");
//    }
    //V3 버전. 유연한 설계 모델앤뷰가 아니라 문자열로 반환해도 됨
    public String newForm(){
        return "new-form";
    }

//    //V2 버전
//    @RequestMapping("/save")
//    public ModelAndView save(HttpServletRequest request, HttpServletResponse response) {
//
//        String username = request.getParameter("username");
//        int age = Integer.parseInt(request.getParameter("age"));
//
//        Member member = new Member(username, age);
//        memberRepository.save(member);
//
//        ModelAndView mav = new ModelAndView("save-result");
//        mav.addObject("member", member);
//        return mav;
//    }

    //v3 버전 우선 @RequestParam을 변수에 쓸 수 있다. 구질구질하게 받는거 없어도 되고, 정수도 파싱따위 필요 없음
    //파라미터로 넘긴 model에 add 어트리뷰트 쓰고, 리턴값으로 스트링 주면 끝
    //@RequestMapping(value = "/save", method = RequestMethod.POST) 와 동의어
    @PostMapping("/save")
    public String save(
            @RequestParam("username") String username,
            @RequestParam("age") int age,
            Model model) {

        Member member = new Member(username, age);
        memberRepository.save(member);

        model.addAttribute("member", member);
        return "save-result";
    }

    //V2 버전
//    @RequestMapping
//    public ModelAndView members() {
//
//        List<Member> members = memberRepository.findAll();
//
//        ModelAndView mav = new ModelAndView("members");
//        mav.addObject("members", members);
//        return mav;
//    }
    // V3 버전 모델만 받아서 뷰 네임만 넘긴다.
    @GetMapping
    public String members(Model model) {
        List<Member> members = memberRepository.findAll();
        model.addAttribute("members", members);
        return "members";
    }

}
