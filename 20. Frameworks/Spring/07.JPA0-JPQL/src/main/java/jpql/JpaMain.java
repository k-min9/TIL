package jpql;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.EntityTransaction;
import javax.persistence.Persistence;
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

            //페이징(몇째부터 몇째까지)

            for (int i = 0; i < 100; i++) {
                Member memberTemp = new Member();
                memberTemp.setUsername("member" + i);
                memberTemp.setAge(i);
                em.persist(memberTemp);
            }

            em.flush();
            em.clear();

            List<Member> result4 = em.createQuery("select m from Member m order by m.age desc", Member.class)
                    .setFirstResult(1)
                    .setMaxResults(10)
                    .getResultList();

            System.out.println("페이징 - result.size() = " + result4.size());
            for (Member member1 : result4) {
                System.out.println("member1 = " + member1);
            }

            // 조인
            Team team = new Team();
            team.setName("teamA");
            em.persist(team);

            member.setTeam(team);

            String query = "select m from Member m inner join m.team t";
            List<Member> result5 = em.createQuery(query, Member.class).getResultList();

            // JPQL 타입 표현 중 Enum (앞의 주소 패키지명(jpql.MemberType)도 다 적어야 한다.)
            String query2 = "select m.username, 'HELLO', true From Member m " +
                    "where m.type = jpql.MemberType.ADMIN";
            
            //case 식
            String query3 = "select" +
                    "case when m.age <= 10 then '학생요금'" +
                    "when m.age>=60 then '경로요금'" +
                    "else '일반요금'" +
                    "end" +
                    "from Member m";


            ////
            tx.commit();
        } catch (Exception e) {
            tx.rollback();
        } finally {
            em.close();
        }
        emf.close();
    }

}