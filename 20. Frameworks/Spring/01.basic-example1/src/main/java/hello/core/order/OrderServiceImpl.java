package hello.core.order;

import hello.core.discount.DiscountPolicy;
import hello.core.discount.FixDiscountPolicy;
import hello.core.discount.RateDiscountPolicy;
import hello.core.member.Member;
import hello.core.member.MemberRepository;
import hello.core.member.MemoryMemberRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
@RequiredArgsConstructor
public class OrderServiceImpl implements OrderService {

    private final MemberRepository memberRepository;
    //private final DiscountPolicy discountPolicy = new FixDiscountPolicy();
    //보기에는 단순하고 잘 된것 같지만, DIP와 OCP 위반
    //private final DiscountPolicy discountPolicy = new RateDiscountPolicy();
    //인터페이스만 의존하도록 코드 변경
    private final DiscountPolicy discountPolicy;

    //생성자 1개면 생략 가능
//    @Autowired
//    public OrderServiceImpl(MemberRepository memberRepository, DiscountPolicy discountPolicy) {
//        this.memberRepository = memberRepository;
//        this.discountPolicy = discountPolicy;
//    }
// RequiredArgConstructor 쓰면 final 관련 필드 생성자 만들어줌

    @Override
    public Order createOrder(Long memberId, String itemName, int itemPrice) {
        Member member = memberRepository.findById(memberId);
        //할인이 디스카운트 내에서만 돌아가고 member에 영향을 끼치지 않음 = 단일 원칙을 잘 지키고 있다.
        int discountPrice = discountPolicy.discount(member, itemPrice);

        return new Order(memberId, itemName, itemPrice, discountPrice);
    }
}
