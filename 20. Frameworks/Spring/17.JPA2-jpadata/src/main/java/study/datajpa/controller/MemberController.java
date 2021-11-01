package study.datajpa.controller;

import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;
import study.datajpa.entity.Member;
import study.datajpa.repository.MemberRepository;

import javax.annotation.PostConstruct;

@RestController
@RequiredArgsConstructor
public class MemberController {

    private final MemberRepository memberRepository;

    @GetMapping("/members/{id}")
    public String findMember (@PathVariable("id") Long id) {
        Member member = memberRepository.findById(id).get();
        return member.getUsername();
    }

    // 도메인 클래스 컨버터 사용시 (스프링 데이터 사용시 알아서 도메인 클래스 컨버터가 동작하여, id를 Member 변환을 해 줌 )
    // >> 조회용, 영속성 컨텍스트 상황 애매
    @GetMapping("/members2/{id}")
    public String findMember2 (@PathVariable("id") Member member) {
        return member.getUsername();
    }

    // 테스트용 기본 값
    @PostConstruct
    public void init() {
        memberRepository.save(new Member("유저A"));

    }

}
