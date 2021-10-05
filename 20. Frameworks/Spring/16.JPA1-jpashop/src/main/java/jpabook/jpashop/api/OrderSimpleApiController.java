package jpabook.jpashop.api;


import jpabook.jpashop.domain.Address;
import jpabook.jpashop.domain.Order;
import jpabook.jpashop.domain.OrderStatus;
import jpabook.jpashop.repository.OrderRepository;
import jpabook.jpashop.repository.OrderSearch;
import jpabook.jpashop.repository.order.simplequery.OrderSimpleQueryDto;
import jpabook.jpashop.repository.order.simplequery.OrderSimpleQueryRepository;

import lombok.Data;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.time.LocalDateTime;
import java.util.List;

import static java.util.stream.Collectors.toList;

/**x to One 관계 최적화*/
// Order -> Member
// Order -> Delivery
@RestController
@RequiredArgsConstructor
public class OrderSimpleApiController {

    private final OrderRepository orderRepository;
    private final OrderSimpleQueryRepository orderSimpleQueryRepository;

    /** V1. 엔티티 직접 노출 */
    //1. Order를 가져올때 Order의 필드인 Member은 LAZY니까 프록시 객체를 가져옴 >> JSON : 응? 얘 뭐임??
    // 해결법-> (Hibernate5Module 모듈 등록, Force_LAZY_ORDER등 사용, 모듈이 LAZY 객체=null 등으로 처리가능)
    //2. 양방향 관계 문제 발생(무한루프 Order->Member->Order...) -> 한쪽에 @JsonIgnore 써야 함
    //3. 애초에 엔티티 외부에 노출하지 말라고!!! (성능 나빠짐, 원하지 않는 정보 노출, 객체 변경시 API 스펙 망가짐...)
    @GetMapping("/api/v1/simple-orders")
    public List<Order> ordersV1() {
        List<Order> all = orderRepository.findAllByCriteria(new OrderSearch());
        // 원하는 애들만 골라서 출력하는 법
        for (Order order : all) {
            order.getMember().getName(); //Lazy 강제 초기화 (getMember까지는 프록시지만 getName 하는 순간 프록시로 처리가 안되니까 쿼리를 날려서 내용물을 등록한다.)
            order.getDelivery().getAddress(); //Lazy 강제 초기화
        }
        return all;
    }

    /** V2. 엔티티를 조회해서 DTO로 변환*/
    //장점 : V1의 문제 대부분 해결
    //단점 : V1과 동일하게 쿼리 1(order 조회)+N(order->member가 order의 결과 수 만큼 실행)+N(order->delivery)번 호출
    @GetMapping("/api/v2/simple-orders")
    public List<SimpleOrderDto> ordersV2() {
        List<Order> orders = orderRepository.findAllByCriteria(new OrderSearch());
        List<SimpleOrderDto> result = orders.stream()
                .map(o -> new SimpleOrderDto(o))
                .collect(toList());

        return result;
    }

    /** V3. 엔티티를 조회해서 DTO로 변환 + fetch join */
    //장점 : 1+N 에러 해결 되고, 단 한번의 쿼리로 모든 정보를 다 가져옴
    //fetch join : 기본편에서 배웠다. 중요도 100%. 우리는 객체가 아닌 객체가 포함된 그림을 넘기는 것이다.
    //단점 : 쿼리시 필요 없는 필드까지 다 긁어온다.
    @GetMapping("/api/v3/simple-orders")
    public List<SimpleOrderDto> ordersV3() {
        List<Order> orders = orderRepository.findAllWithMemberDelivery();
        List<SimpleOrderDto> result = orders.stream()
                .map(o -> new SimpleOrderDto(o))
                .collect(toList());
        return result;
    }

    /** v4. 엔티티에서 DTO 변환 없이, DTO 바로 조회*/
    //장점 : V3의 단점 조차 없어지면서 더 최적화
    //단점 : 재활용하기 힘든 코드...
    @GetMapping("/api/v4/simple-orders")
    public List<OrderSimpleQueryDto> ordersV4() {
        return orderSimpleQueryRepository.findOrderDtos();
    }


    @Data
    static class SimpleOrderDto {

        private Long orderId;
        private String name;
        private LocalDateTime orderDate; //주문시간
        private OrderStatus orderStatus;
        private Address address;

        public SimpleOrderDto(Order order) {
            orderId = order.getId();
            name = order.getMember().getName(); // 프록시 내용물 참조로 멤버쿼리 > LAZY 강제 초기화
            orderDate = order.getOrderDate();
            orderStatus = order.getStatus();
            address = order.getDelivery().getAddress();
        }
    }

}
