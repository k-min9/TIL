package hello.core.discount;

import hello.core.member.Grade;
import hello.core.member.Member;

// VIP면 천원 할인
public class FixDiscountPolicy implements DiscountPolicy{

    private int discountFixAmount = 1000; //천원 할인

    @Override
    public int discount(Member member, int price) {
        if (member.getGrade() == Grade.VIP){
            return discountFixAmount;
        } else{
            return 0;
        }
    }
}
