package jpabook.jpashop.service;

import jpabook.jpashop.domain.Member;
import jpabook.jpashop.repository.MemberRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
@Transactional(readOnly = true) // 기본적으로 트랜잭션 안에서만 데이터 변경 (옵션 : 데이터 변경이 안되는 대신에 최적화 되어 읽는게 빨라짐)
@RequiredArgsConstructor
public class MemberService {

    // 주입이 안되면 컴파일 시점에서 체크해주니까 final 넣으면 좋음
    private final MemberRepository memberRepository;

    // 이거 전부 RequiredArgsConstructor 가 처리해줌
//    //testcase 작성 및 변경을 고려해서 생성자에서 주입을 한다.
//    @Autowired  // 생성자 하나니까 생략 가능
//    public MemberService(MemberRepository memberRepository) {
//        this.memberRepository = memberRepository;
//    }

    //회원 가입
    @Transactional // 이러면 readonly true보다 자세한 값이 이 값이 우선되어 기본값인 false가 들어간다.
    public Long join(Member member){
        validateDuplicateMember(member);
        memberRepository.save(member);
        return member.getId();
    }

    //중복 회원 검증 로직
    private void validateDuplicateMember(Member member) {
        //실무에서는 동시 호출시나 멀티스레드를 고려해서 getName을 unique 제약으로 잡는것을 추천
        List<Member> findMembers = memberRepository.findByName(member.getName());
        if (!findMembers.isEmpty()) {
            throw new IllegalStateException("이미 존재하는 회원입니다.");
        }
    }

    //회원 전체 조회
    public List<Member> findMembers() {
        return memberRepository.findAll();
    }

    //회원 단 건 조회
    public Member findOne(Long memberId) {
        return memberRepository.findOne(memberId);
    }

    //api용: @Transactional > 트랜잭션 시작 > 찾아서 영속성 컨텍스트에 > 트랜잭션 종료되면서 커밋되고 flush
    @Transactional
    public void update(Long id, String name) {
        Member member = memberRepository.findOne(id);
        member.setName(name);
    }
}
