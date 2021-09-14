package jpabook.jpashop.domain;

import javax.persistence.Column;
import javax.persistence.Embeddable;
import java.util.Objects;

//Delivery 필드를 묶어서 값타입 생성
@Embeddable
public class Address {

    // 관리도 가능
    @Column(length = 10)
    private String city;
    private String street;
    @Column(length = 200)
    private String zipcode;

    //값 타입시 특정 타입과 관련된 밀접된 비지니스 메소드 제작도 가능하다
    public String fullAddress(){
        return getCity() + " " + getStreet() + " " + getZipcode();
    }

    public String getCity() {
        return city;
    }

    // 불변객체로 만들게 접근 막기
    private void setCity(String city) {
        this.city = city;
    }

    public String getStreet() {
        return street;
    }

    private void setStreet(String street) {
        this.street = street;
    }

    public String getZipcode() {
        return zipcode;
    }

    private void setZipcode(String zipcode) {
        this.zipcode = zipcode;
    }

    //프록시일때도 접근하려면 getter 옵션 켜줘라
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Address address = (Address) o;
        return Objects.equals(getCity(), address.getCity()) && Objects.equals(getStreet(), address.getStreet()) && Objects.equals(getZipcode(), address.getZipcode());
    }

    @Override
    public int hashCode() {
        return Objects.hash(getCity(), getStreet(), getZipcode());
    }
}
