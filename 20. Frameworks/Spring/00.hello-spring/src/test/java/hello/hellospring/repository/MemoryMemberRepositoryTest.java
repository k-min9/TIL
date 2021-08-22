package hello.hellospring.repository;

import hello.hellospring.domain.Member;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

//add-on static 예제
import java.util.List;

import static org.assertj.core.api.Assertions.*;

class MemoryMemberRepositoryTest {

    MemoryMemberRepository repository = new MemoryMemberRepository();

    @AfterEach
    public void afterEach(){
        repository.clearStore();
    }

    @Test
    public void save(){
        Member member = new Member();
        member.setName("강민구");

        repository.save(member);

        //저장할때 만들어진 key로 꺼낸 것과 집어 넣기 전에 저장한 내용 비교
        Member result = repository.findById(member.getId()).get();
        //System.out.println("result = " + (result == member));
        //Assertion 임포트 종류가 다름
        Assertions.assertEquals(member, result);
        //Assertions.assertEquals(member, null);
        assertThat(member).isEqualTo(result);
    }

    @Test
    public void findByName(){
        Member member1 = new Member();
        member1.setName("강민구1");
        repository.save(member1);

        Member member2 = new Member();
        member2.setName("강민구2");
        repository.save(member2);

        Member result = repository.findByName("강민구1").get();

        assertThat(result).isEqualTo(member1);
    }

    @Test
    public void findAll() {

        Member member1 = new Member();
        member1.setName("강민구3");
        repository.save(member1);
        Member member2 = new Member();
        member2.setName("강민구4");
        repository.save(member2);

        List<Member> result = repository.findAll();

        assertThat(result.size()).isEqualTo(2);
    }
}
