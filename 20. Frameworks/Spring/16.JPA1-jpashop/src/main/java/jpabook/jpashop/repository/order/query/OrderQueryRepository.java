package jpabook.jpashop.repository.order.query;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Repository;

import javax.persistence.EntityManager;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

@Repository
@RequiredArgsConstructor
public class OrderQueryRepository {

    private final EntityManager em;

    public List<OrderQueryDto> findOrderQueryDtos() {
        // extract method 안하고 그냥 보겠음
        List<OrderQueryDto> result = em.createQuery(
                //우리들이 querydsl을 배워야 하는 이유
                "select new jpabook.jpashop.repository.order.query.OrderQueryDto(o.id, m.name, o.orderDate, o.status, d.address)" + //(쿼리 1회)
                        "from Order o" +
                        "join o.member m" +
                        "join o.delivery d", OrderQueryDto.class)
                .getResultList();

        //"select new jpabook.jpashop.repository.order.query.OrderQuertDto(o.id, m.name, o.orderDate, o.status, d.address)" 보면 알겠지만 컬렉션 부분 없음
        //루프를 돌면서 컬렉션 직접 추가
        result.forEach(o -> {
            List<OrderItemQueryDto> orderItems = findOrderItems(o.getOrderId()); //(쿼리 N회)
            o.setOrderItems(orderItems);
        });
        return result;
    }

    private List<OrderItemQueryDto> findOrderItems(Long orderId) {
        return em.createQuery(
                        "select new jpabook.jpashop.repository.order.query.OrderItemQueryDto(oi.order.id, i.name, oi.orderPrice, oi.count)" +
                                " from OrderItem oi" +
                                " join oi.item i" +
                                " where oi.order.id = : orderId", OrderItemQueryDto.class)
                .setParameter("orderId", orderId)
                .getResultList();
    }

     // ordersV5
     // Query: 루트 1번, 컬렉션 1번로 최적화
     // 데이터를 한꺼번에 처리할 때 많이 사용하는 방식
    public List<OrderQueryDto> findAllByDto_optimization() {
        // extract method 안하고 그냥 보겠음
        List<OrderQueryDto> result = em.createQuery(
                        //우리들이 querydsl을 배워야 하는 이유
                        "select new jpabook.jpashop.repository.order.query.OrderQueryDto(o.id, m.name, o.orderDate, o.status, d.address)" + //(쿼리 1회)
                                "from Order o" +
                                "join o.member m" +
                                "join o.delivery d", OrderQueryDto.class)
                .getResultList();
        // 여기까지는 findOrderQueryDtos과 동일

        //orderIds(orderId의 리스트) 만들기
        List<Long> orderIds = result.stream()
                        .map(o-> o.getOrderId())
                        .collect(Collectors.toList());

        // 주문서와 관련된 orderItem
        List<OrderItemQueryDto> orderItems = em.createQuery(
                        "select new jpabook.jpashop.repository.order.query.OrderItemQueryDto(oi.order.id, i.name, oi.orderPrice, oi.count)" +
                                " from OrderItem oi" +
                                " join oi.item i" +
                                " where oi.order.id in : orderId", OrderItemQueryDto.class) // findOrderItems 에서 사용한 = 이 아니라 in을 써서 한번에 가져온다.
                .setParameter("orderId", orderIds)
                .getResultList();

        // orderItem을 map으로 바꾸자 (루프 돌리면 좋지만 이게 더 편함)
        Map<Long, List<OrderItemQueryDto>> orderItemMap = orderItems.stream()
                .collect(Collectors.groupingBy(orderItemQueryDto -> orderItemQueryDto.getOrderId()));

        // key를 value로 쭉 돌림
        result.forEach(o -> o.setOrderItems(orderItemMap.get(o.getOrderId())));

        // 여태까지 쿼리 딱 두 번 돌렸음을 알 수 있다.
        return result;
    }

}
