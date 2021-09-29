package jpabook.jpashop.domain;

import lombok.Getter;

import javax.persistence.Embeddable;


@Embeddable
@Getter //값 타입은 기본 Getter만 두고, 값 변경은 불변객체로 덮어쓴다.(참조 관련 오류 방지)
public class Address {

    private String City;
    private String street;
    private String zipcode;

    //이렇게 protected 설정시 값 타입 호출 관련 오류가 뜨니까 편하다.
    protected Address() {
    }

    public Address(String city, String street, String zipcode) {
        City = city;
        this.street = street;
        this.zipcode = zipcode;
    }
}
