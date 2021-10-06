package jpabook.jpashop.api;

import jpabook.jpashop.domain.Address;
import jpabook.jpashop.domain.Order;
import jpabook.jpashop.domain.OrderItem;
import jpabook.jpashop.domain.OrderStatus;
import jpabook.jpashop.repository.OrderRepository;
import jpabook.jpashop.repository.order.query.OrderQueryDto;
import jpabook.jpashop.repository.order.query.OrderQueryRepository;
import lombok.Data;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.time.LocalDateTime;
import java.util.List;

import static java.util.stream.Collectors.toList;

/**일대다(컬렉션 조회) 최적화*/
@RestController
@RequiredArgsConstructor
public class OrderApiController {

    private final OrderRepository orderRepository;
    private final OrderQueryRepository orderQueryRepository;

    /**V1. 엔티티 직접 노출*/
    //단점 : 너무 많아서 생략
    @GetMapping("/api/v1/orders")
    public List<Order> ordersV1() {
        List<Order> all = orderRepository.findAll();
        for (Order order : all) {
            order.getMember().getName(); //Lazy 강제 초기화
            order.getDelivery().getAddress(); //Lazy 강제 초기화

            //프록시가 아니라 orderitems 내용물을 보고 싶으니 강제 초기화 해서 봅시다.
            List<OrderItem> orderItems = order.getOrderItems();
            orderItems.stream().forEach(o -> o.getItem().getName()); //Lazy 강제 초기화
        }
        return all;
    }

    /** V2. 엔티티를 조회해서 DTO로 변환*/
    //단점 : 1+N(order->member, order -> address)+N(order->orderItem)+N(orderItem->item)회 쿼리 나감 = 난리남
    @GetMapping("/api/v2/orders")
    public List<OrderDto> ordersV2() {
        List<Order> orders = orderRepository.findAll();
        List<OrderDto> result = orders.stream()
                .map(o -> new OrderDto(o))
                .collect(toList());

        return result;
    }

    /** V3. 엔티티를 조회해서 DTO로 변환 + fetch join*/
    //장점 : 쿼리 1번으로 V2와 같은 쿼리를 다 처리할 수 있다.
    //단점 : 일대다는 fetch join 하는 순간 페이징이 불가능해진다.
    // 1. order가 join하면서 내용이 뻥튀기(row 증가) 되고, order 순서 자체가 뒤틀린다.
    // 2. 그래서 해야되면 뻥튀기 된 자료를 메모리에 나열해서 소트 = 아웃 오브 메모리 나기 딱
    @GetMapping("/api/v3/orders")
    public List<OrderDto> ordersV3() {
        List<Order> orders = orderRepository.findAllWithItem();
        List<OrderDto> result = orders.stream()
                .map(o -> new OrderDto(o))
                .collect(toList());

        return result;
    }

    /**
     * V3.1 엔티티를 조회해서 DTO로 변환 페이징 고려
     * - ToOne 관계만 우선 모두 페치 조인으로 최적화
     * - 컬렉션 관계는 hibernate.default_batch_fetch_size, @BatchSize로 최적화
     */
    //장점 : 1+N 쿼리를 1+1(N//1000) 으로 변경, hibernate.default_batch_fetch_size만큼 보내니까 DB 데이터 전송량 최적화
    @GetMapping("/api/v3.1/orders")
    public List<OrderDto> ordersV3_page(@RequestParam(value = "offset", defaultValue = "0") int offset,
                                        @RequestParam(value = "limit", defaultValue = "100") int limit) {

        List<Order> orders = orderRepository.findAllWithMemberDelivery(offset, limit);
        List<OrderDto> result = orders.stream()
                .map(o -> new OrderDto(o))
                .collect(toList());

        return result;
    }



    /** V4. JPA에서 DTO로 바로 조회, 컬렉션 N 조회 (1 + N Query)*/
    @GetMapping("/api/v4/orders")
    public List<OrderQueryDto> ordersV4() {
        return orderQueryRepository.findOrderQueryDtos();
    }






    @Data //까먹고 안하면 no property 뜨더라
    static class OrderDto {

        private Long orderId;
        private String name;
        private LocalDateTime orderDate; //주문시간
        private OrderStatus orderStatus;
        private Address address;
        private List<OrderItemDto> orderItems;

        public OrderDto(Order order) {
            orderId = order.getId();
            name = order.getMember().getName();
            orderDate = order.getOrderDate();
            orderStatus = order.getStatus();
            address = order.getDelivery().getAddress();
            //order.getOrderItems() 하면 null이 뜬다. 그야 엔티티니까. 프록시가 들어가 있겠지. 초기화 필요.
            orderItems = order.getOrderItems().stream()
                    .map(orderItem -> new OrderItemDto(orderItem))
                    .collect(toList());
        }
    }

    // 단순히 DTO로 감싸는게 아니라, 엔티티를 이렇게 DTO로 뽑아야 엔티티 노출을 막으며 원하는 값을 출력할 수 있다.
    // 콜렉션은 귀찮지만 이렇게 다 감싸줘야 함. 현업들이 자주 하는 실수이므로 주의(V2 강좌 강조 지점)
    @Data
    static class OrderItemDto {

        private String itemName;//상품 명
        private int orderPrice; //주문 가격
        private int count;      //주문 수량

        public OrderItemDto(OrderItem orderItem) {
            itemName = orderItem.getItem().getName();
            orderPrice = orderItem.getOrderPrice();
            count = orderItem.getCount();
        }
    }

}
