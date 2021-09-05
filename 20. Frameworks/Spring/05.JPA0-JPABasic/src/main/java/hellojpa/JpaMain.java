package hellojpa;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.EntityTransaction;
import javax.persistence.Persistence;

public class JpaMain {

    public static void main(String[] args) {
        // 퍼시스턴트 유닛 네임을 변수로
        // 이 시점에서 DB연결은 끝남
        // 시작할때 반드시 하나만 만들어줘야 됨
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello");

        // em팩토리에서 em 생성, 트랜잭션 등의 행동 마다 하나씩 만들면 됨. 쓰고 버린다.
        EntityManager em = emf.createEntityManager();

        //모든 행동은 트랜잭션 내에서 일어난다.
        EntityTransaction tx = em.getTransaction();
        tx.begin();

        try {
            //C
//            Member member = new Member();
//            member.setId(2L);
//            member.setName("HelloB");

            //저장(영속) 같은것이라고 생각하면 됨 (>> 엔티티를 엔티티 영속성 컨테스트라는 곳에 저장한다)
//            em.persist(member);

            //R:찾기 예제
//            Member findmember = em.find(Member.class, 1L);
//            System.out.println("findmember = " + findmember.getName());

            //U:수정 예제 (persist 필요 없음)
//            findmember.setName("HelloJPA");

           //D:삭제 예제
//            em.remove(findmember);

            tx.commit();
        } catch (Exception e) {
            tx.rollback();
        } finally {
            // 다 끝나면 닫아줘야 됨
            em.close();
        }

        // 다 끝나면 닫아줘야 됨
        emf.close();
    }

}
