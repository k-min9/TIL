package study.datajpa.controller;

import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;
import study.datajpa.dto.MemberDto;
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

    /** controller web 페이징과 소팅 : Page로 반환하면 스프링 데이터가 알아서 해준다. */
    // members?page=0&size=3&sort=id,desc&sort=username,desc : 0페이지 3개씩 끊어서, id, username순으로 내림 정렬 등에 대응
    @GetMapping("/members")
    // 기본 사이즈 조절시 Pageable앞에 @Param 붙이듯이,
    // @PageableDefault(size = 5, sort = "username") 이런식으로 붙일수 있음
    public Page<MemberDto> list(Pageable pageable)
    {
        Page<Member> page = memberRepository.findAll(pageable);
        // 당연히 DTO로 반환해야 한다.
        Page<MemberDto> map = page.map(member -> new MemberDto(member.getId(), member.getUsername(), null));
        return map;
    }


//    테스트용 기본 값 (다른 예제, 특히 save 관련 방해되니까 비활성화)
//    @PostConstruct
    public void init() {
        memberRepository.save(new Member("유저A"));
        for (int i = 0; i< 100; i++) {
            memberRepository.save(new Member("user"+i, i));
        }

    }

}
