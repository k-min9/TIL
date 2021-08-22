package hello.hellospring.repository;

import hello.hellospring.domain.Member;

import javax.persistence.EntityManager;
import java.util.List;
import java.util.Optional;

public class JpaMemberRepository implements MemberRepository{

    //jpa는 entitymanager로 작업을 제어
    private final EntityManager em;

    public JpaMemberRepository(EntityManager em) {
        this.em = em;
    }

    @Override
    public Member save(Member member) {
        //더 짧아졌다. persist 는 영구적 저장이라는 뜻
        em.persist(member);
        return member;
    }

    @Override
    public Optional<Member> findById(Long id) {
        Member member = em.find(Member.class, id);
        return Optional.ofNullable(member);
    }

    @Override
    public Optional<Member> findByName(String name) {
        List<Member> result = em.createQuery("select m from Member m where m.name = :name", Member.class)
                .setParameter("name", name)
                .getResultList();
        return result.stream().findAny();
    }

    @Override
    public List<Member> findAll() {
        //객체를 대상으로 한 쿼리를 함 Member m 은 Member as m의 단축
        List<Member> result = em.createQuery("select m from Member m", Member.class).getResultList();
        return result;
        //반환이 result처럼 단순하면, (alt + enter) 인라인 배리어블 해서 이렇게 한줄로 바꿀 수 있음
        //return em.createQuery("select m from Member m", Member.class).getResultList();
    }
}
