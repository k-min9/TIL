package hello.login;

import hello.login.domain.item.Item;
import hello.login.domain.item.ItemRepository;
import hello.login.domain.member.Member;
import hello.login.domain.member.MemberRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;

//테스트용 선 입력 데이터
@Component
@RequiredArgsConstructor
public class TestDataInit {

    private final ItemRepository itemRepository;
    private final MemberRepository memberRepository;

    @PostConstruct//의존성 주입 후 초기화 수행할때 메서드를 수행하게 하는 애노테이션
    public void init() {
        //상품 데이터
        itemRepository.save(new Item("itemA", 10000, 10));
        itemRepository.save(new Item("itemB", 20000, 20));

        //회원 데이터
        Member member = new Member();
        member.setLoginId("mingu4969");
        member.setPassword("test!");
        member.setName("강민구");

        memberRepository.save(member);




    }

}