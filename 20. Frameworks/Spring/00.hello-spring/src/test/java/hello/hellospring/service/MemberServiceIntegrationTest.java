package hello.hellospring.service;

import hello.hellospring.domain.Member;
import hello.hellospring.repository.MemberRepository;
import hello.hellospring.repository.MemoryMemberRepository;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.annotation.Commit;
import org.springframework.transaction.annotation.Transactional;

import static org.junit.jupiter.api.Assertions.assertThrows;

@SpringBootTest
@Transactional
class MemberServiceIntegrationTest {

    //MemberService memberService = new MemberService();
    //MemoryMemberRepository memoryMemberRepository = new MemoryMemberRepository();    //clear용
    //Constructor로 원본 변경
    @Autowired MemberService memberService;
    @Autowired  MemberRepository memberRepository;    //clear용

    @Test
    //@Commit 붙이면 그 결과가 반영이됨
    void join() {
        //given
        Member member = new Member();
        member.setName("hello2");

        //when
        Long saveId = memberService.join(member);

        //then
        Member findMember = memberService.findOne(saveId).get();
        Assertions.assertThat(member.getName()).isEqualTo(findMember.getName());
    }

    // 테스트는 이름 한국어로 짓는다던가 테스트자체에 문제가 없으면 직관성추구 이름을 지어도 된다.
    @Test
    public void 중복회원예외(){
        //given
        Member member1 = new Member();
        member1.setName("강민구5");

        Member member2 = new Member();
        member2.setName("강민구5");

        //when
        //방법2 assertThrow로 exception 종류 확인 후, assertThat으로 메시지 확인
        memberService.join(member1) ;
        //저 exception이 나오나 확인
        IllegalStateException e = assertThrows(IllegalStateException.class, () -> memberService.join(member2));
        Assertions.assertThat(e.getMessage()).isEqualTo("이미 존재하는 회원입니다.");

        /* 방법 1 Try Catch
        memberService.join(member1);
        try{
            memberService.join(member2);
            fail();
        } catch (IllegalStateException e) {
            Assertions.assertThat(e.getMessage()).isEqualTo("이미 존재하는 회원입니다.");
        }
        */


        //then

    }

    @Test
    void findMembers() {
    }

    @Test
    void findOne() {
    }
}