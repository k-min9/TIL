package jpabook.jpashop.repository;

import jpabook.jpashop.domain.Member;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Repository;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import java.util.List;

@Repository
@RequiredArgsConstructor
public class MemberRepository {

    //스프링이 em을 만들고 주입하게 설정 (필드 주입 -> 생성자 주입하여서 RequiredArgsConstructor 사용)
    //@PersistenceContext (스프링 부트에서는 @Autowired로 갈음 가능. 그래서 RequiredArgsConstructor 이거 사용 가능)
    private final EntityManager em;

    public void save(Member member){
        em.persist(member);
    }

    public Member findOne(Long id){
        return em.find(Member.class, id);
    }

    public List<Member> findAll() {

        return em.createQuery("select m from Member m", Member.class)
                .getResultList();
    }

    public List<Member> findByName(String name) {
        return em.createQuery("select m from Member m where m.name = : name", Member.class)
                .setParameter("name", name)
                .getResultList();
    }


}
