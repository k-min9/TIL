package jpabook.jpashop.domain;

import javax.persistence.*;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

@Entity
@Table(name = "ORDERS")
public class Order extends BaseEntity{

    @Id @GeneratedValue
    @Column(name = "ORDER_ID")
    private Long id;

//    @Column(name = "MEMBER_ID")
//    private Long MemberId;

    //MEMBER과 ORDERS의 단방향 연결
    @ManyToOne(fetch = FetchType.LAZY) // one to one , many to one은 무조건 지연로딩으로 바꿔야한다.
    @JoinColumn(name = "MEMBER_ID") //외래키 기준
    private Member member;

    // 1:1 관계
    @OneToOne(fetch = FetchType.LAZY, cascade = CascadeType.ALL) // order시 생성되는 delivery에는 아예 영속성전이 ALL
    @JoinColumn(name = "DELIVERY_ID")
    private Delivery delivery;

    //역방향 연결 => 주인 OrderItem의 order
    @OneToMany(mappedBy = "order", cascade = CascadeType.ALL)
    private List<OrderItem> orderItems = new ArrayList<>();

    private LocalDateTime orderDate;

    @Enumerated(EnumType.STRING) // 안하면 나중에 큰 장애 가능성 있음
    private OrderStatus status;

    // 양방향 편의 메소드 구현
    public void addOrderItem(OrderItem orderItem) {
        orderItems.add(orderItem);
        orderItem.setOrder(this);
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Member getMember() {
        return member;
    }

    public void setMember(Member member) {
        this.member = member;
    }

    public LocalDateTime getOrderDate() {
        return orderDate;
    }

    public void setOrderDate(LocalDateTime orderDate) {
        this.orderDate = orderDate;
    }

    public OrderStatus getStatus() {
        return status;
    }

    public void setStatus(OrderStatus status) {
        this.status = status;
    }


}
