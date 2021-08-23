package hello.core.discount;

import hello.core.member.Member;

public interface DiscountPolicy {

    //할인 대상 금액
    int discount(Member member, int price);
}
