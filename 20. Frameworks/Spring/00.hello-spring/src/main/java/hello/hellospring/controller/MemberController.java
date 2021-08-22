package hello.hellospring.controller;


import hello.hellospring.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;

@Controller
public class MemberController {

    //어차피 하나면 되니까 여기 등록해서 쓴다.
    private final MemberService memberService;

    //생성자(Alt+insert에서 constuctor)로 연결
    @Autowired
    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }
}
