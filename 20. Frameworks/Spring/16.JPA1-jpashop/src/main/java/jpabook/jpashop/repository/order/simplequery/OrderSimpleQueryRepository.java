package jpabook.jpashop.repository.order.simplequery;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Repository;

import javax.persistence.EntityManager;
import java.util.List;

//OrderRepository에 두면 이것밖에 못하는 애가 자리 차지하고 어중간하니까 아예 분리하여서 조회 전용으로 사용
@Repository
@RequiredArgsConstructor
public class OrderSimpleQueryRepository {

    private final EntityManager em;

    public List<OrderSimpleQueryDto> findOrderDtos() {
        return em.createQuery(
                    //new로 JPQL 결과를 직접 DTO로 생성
                    //o로 못 넣고 파라미터를 주소까지 포함해서 일일히 다 집어 넣어줘야 함...
                        "select new jpabook.jpashop.repository.order.simplequery.OrderSimpleQueryDto(o.id, m.name, o.orderDate, o.status, d.address)" +
                                " from Order o" +
                                " join o.member m" +
                                " join o.delivery d", OrderSimpleQueryDto.class)
                .getResultList();
    }
}
