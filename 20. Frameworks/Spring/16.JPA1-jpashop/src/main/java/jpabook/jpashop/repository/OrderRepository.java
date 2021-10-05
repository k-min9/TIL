package jpabook.jpashop.repository;

import jpabook.jpashop.domain.Order;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Repository;
import org.springframework.util.StringUtils;

import javax.persistence.EntityManager;
import javax.persistence.TypedQuery;
import javax.persistence.criteria.*;
import java.util.ArrayList;
import java.util.List;

@Repository
@RequiredArgsConstructor
public class OrderRepository {

    private final EntityManager em;

    public void save(Order order) {
        em.persist(order);
    }

    public Order findOne(Long id) {
        return em.find(Order.class, id);
    }

    //검색 로직(이건 누락이나 문제가 없거나 하는 이상적인 경우고 실제로는 쓸 수 없다. 그렇다고 jpql 부분 문자열을 조립하는건 비효율+오류 투성이)
//    public List<Order> findAll(OrderSearch orderSearch){
//        em.createQuery("select o from Order o join o.member m"
//                + "where o.status = :status"
//                + "and m.name like :name", Order.class)
//                .setParameter("status", orderSearch.getOrderStatus())
//                .setParameter("name", orderSearch.getMemberName())
//                .setMaxResults(1000) // 최대 1000건
//                .getResultList();
//
//    }

    //Criteria : JPA가 제공하는 동적 쿼리 빌드 (이것도 비권장 = 실무 비적합)
    //이게 무슨 쿼리인지 안떠오르는 가독성 = 유지보수가 힘듬,
    public List<Order> findAllByCriteria(OrderSearch orderSearch) {
        CriteriaBuilder cb = em.getCriteriaBuilder();
        CriteriaQuery<Order> cq = cb.createQuery(Order.class);
        Root<Order> o = cq.from(Order.class);
        Join<Object, Object> m = o.join("member", JoinType.INNER);

        List<Predicate> criteria = new ArrayList<>();

        //주문 상태 검색
        if (orderSearch.getOrderStatus() != null) {
            Predicate status = cb.equal(o.get("status"), orderSearch.getOrderStatus());
            criteria.add(status);
        }
        //회원 이름 검색
        if (StringUtils.hasText(orderSearch.getMemberName())) {
            Predicate name =
                    cb.like(m.<String>get("name"), "%" + orderSearch.getMemberName() + "%");
            criteria.add(name);
        }

        cq.where(cb.and(criteria.toArray(new Predicate[criteria.size()])));
        TypedQuery<Order> query = em.createQuery(cq).setMaxResults(1000);
        return query.getResultList();
    }

    /// 최종적으로 쿼리 DSL로 해결할 것이다. 여기서는 교육은 없고고 예시로보여드림


    // api용 fetch join(기본편에서 배웠다. 우리는 객체가 아닌 객체가 포함된 그림을 넘기는 것이다.)
    public List<Order> findAllWithMemberDelivery() {
        return em.createQuery(
                        "select o from Order o" +
                                " join fetch o.member m" +
                                " join fetch o.delivery d", Order.class)
                .getResultList();
    }



}
