package jpabook.jpashop.repository.order.query;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Repository;

import javax.persistence.EntityManager;
import java.util.List;

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
}
