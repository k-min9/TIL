package hello.hellospring.service;

import hello.hellospring.domain.Member;
import hello.hellospring.repository.MemberRepository;
import hello.hellospring.repository.MemoryMemberRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

//@Service
public class MemberService {

    //1. 일반 구축
    //private final MemberRepository memberRepository = new MemoryMemberRepository();
    //2. 테스트 용으로 constructor 사용
    private final MemberRepository memberRepository;

    //@Autowired
    public MemberService(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

    //회원 가입
    public Long join(Member member){

        //예시 같은 이름의 회원은 안된다.
//        Optional<Member> result = memberRepository.findByName(member.getName());
//        result.ifPresent(m -> {throw new IllegalStateException("이미 존재하는 회원입니다.");});
        //위에거 줄여서 이렇게 표현 가능 >> extract method = Shift + Ctrl + Alt + T
        validateDuplicateMember(member);

        memberRepository.save(member);
        return member.getId();
    }

    private void validateDuplicateMember(Member member) {
        memberRepository.findByName(member.getName()).
                ifPresent(m ->
                    {throw new IllegalStateException("이미 존재하는 회원입니다.");
                });
    }
    
    //전체 회원 조회
    public List<Member> findMembers(){
        return memberRepository.findAll();
    }

    //하나 조회
    public Optional<Member> findOne(Long memberId){
        return memberRepository.findById(memberId);
    }


}
