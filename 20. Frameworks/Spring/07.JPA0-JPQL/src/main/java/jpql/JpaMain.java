package jpql;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.EntityTransaction;
import javax.persistence.Persistence;
import java.sql.SQLOutput;
import java.util.List;

public class JpaMain {

    public static void main(String[] args) {
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello");
        EntityManager em = emf.createEntityManager();

        EntityTransaction tx = em.getTransaction();
        tx.begin();

        try {
            Member member = new Member();
            member.setUsername("member1");
            member.setAge(10);
            em.persist(member);

            em.flush();
            em.clear();

            //엔티티 조회
            List<Team> result = em.createQuery("select t from Member m join m.team t", Team.class)
                    .getResultList();
            
            //임베디드 조회(엔티티와 비슷하니 생략)

            //스칼라 조회(값 여럿) 방법 1
            List result2 = em.createQuery("select m.username, m.age from Member m")
                    .getResultList();

            Object o = result2.get(0);
            Object[] result2List = (Object[]) o;
            System.out.println("username = " + result2List[0]);
            System.out.println("age = " + result2List[1]);

            //스칼라 조회(값 여럿) 방법 2
            List<MemberDTO> result3 = em.createQuery("select new jpql.MemberDTO(m.username, m.age) from Member m", MemberDTO.class)
                    .getResultList();

            MemberDTO memberDTO = result3.get(0);
            System.out.println("usernameDTO = " + memberDTO.getUsername());
            System.out.println("ageDTO = " + memberDTO.getAge());

            tx.commit();
        } catch (Exception e) {
            tx.rollback();
        } finally {
            em.close();
        }
        emf.close();
    }

}