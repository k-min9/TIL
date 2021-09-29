package jpabook.jpashop.domain;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Entity
@Getter @Setter
public class Member {

    @Id @GeneratedValue
    @Column(name = "member_id")
    private Long id;

    private String name;

    @Embedded  //Embeddable, Embedded 둘 중 하나만 하지만 일반적으로는 둘 다 적어준다.
    private Address address;

    @OneToMany(mappedBy = "member") //이제부터 member가 관리하고 읽기 전용처럼 쓴다고 생각하면 편하다.
    private List<Order> orders = new ArrayList<>();

    //연관관계 메서드


}
