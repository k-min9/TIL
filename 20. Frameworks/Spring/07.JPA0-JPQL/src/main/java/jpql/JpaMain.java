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
            member.setUsername("회원 강민구");
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
            for (Member member4 : result4) {
                System.out.println("member4 = " + member4);
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

            // 페치 조인(매우 중요!!!!)
            Team teamA = new Team();
            teamA.setName("팀A");
            em.persist(teamA);

            Team teamB = new Team();
            teamB.setName("팀B");
            em.persist(teamB);

            Member member1 = new Member();
            member1.setUsername("회원1");
            member1.setTeam(teamA);
            em.persist(member1);

            Member member2 = new Member();
            member2.setUsername("회원2");
            member2.setTeam(teamA);
            em.persist(member2);

            Member member3 = new Member();
            member3.setUsername("회원3");
            member3.setTeam(teamB);
            em.persist(member3);

            em.flush();
            em.clear();

            //기존 > 처음(SQL), A(SQL), A(1차 캐시), B(SQL) - 총 3회 쿼리 발생
            //페치 : 1회 SQL로 필요한 데이터를 다 가져옴
            String queryFetch = "select m from Member m join fetch m.team";
            List<Member> resultFetch = em.createQuery(queryFetch, Member.class).getResultList();

            for (Member memberFetch : resultFetch) {
                System.out.println("member = " + memberFetch.getUsername()+", "+memberFetch.getTeam());
            }
            //페치는 다대일은 상관없지만, 1대다 같은 경우에는 데이터 뻥튀기가 발생할 수 있어서, 필요시 JPQL DISTINCT로 같은 식별자 제거 가능

            //네임드 쿼리 : 로딩 시점 초기화+파싱+캐시 and 로딩 시점 쿼리 검증
            List<Member> queryNamedResult = em.createNamedQuery("Member.findByUsername", Member.class)
                    .setParameter("username", "회원 1")
                    .getResultList();

            for (Member member5 : queryNamedResult) {
                System.out.println("네임드 쿼리 member = " + member5);
            }

            //벌크 연산 (executeupdate) : 쿼리 한번에 여러 테이블의 row를 변경
            em.createQuery("update Member m set m.age = 20").executeUpdate();

            System.out.println("member1.getAge() = " + member1.getAge()); // 영속성 컨텍스트 값인 0으로 나옴 DB는 20이 반영됨
            System.out.println("member2.getAge() = " + member2.getAge());

            em.clear(); // 벌크 연산전 flush는 실행되지만, 변경된 DB와 영속성컨텍스트의 값이 일치하지 않게 되기 때문에 초기화 해야한다.

            Member findMember = em.find(Member.class, member1.getId());
            System.out.println("member1의 DB값.getAge() = " + findMember.getAge());


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