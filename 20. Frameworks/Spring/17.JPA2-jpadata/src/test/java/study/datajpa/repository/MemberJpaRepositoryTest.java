package study.datajpa.repository;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.annotation.Rollback;
import org.springframework.transaction.annotation.Transactional;
import study.datajpa.entity.Member;

import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
@Transactional  // org. // 모든 데이터 변경은 Transactional 내부에서 일어나니까 필수
@Rollback(false)  // 이거 해둬야 롤백 안하고 DB에 결과가 남아서 내용 볼 수 있음
class MemberJpaRepositoryTest {

    @Autowired
    MemberJpaRepository memberJpaRepository;

    @Test
    public void testMember(){
        Member member = new Member("memberA");
        Member savedmember = memberJpaRepository.save(member);

        Member findmember = memberJpaRepository.find(savedmember.getId());

        assertThat(findmember.getId()).isEqualTo(member.getId());
        assertThat(findmember.getUsername()).isEqualTo(member.getUsername());
        assertThat(findmember).isEqualTo(member);
    }

    @Test
    public void paging() throws Exception {
        //given
        memberJpaRepository.save(new Member("member1", 10));
        memberJpaRepository.save(new Member("member2", 10));
        memberJpaRepository.save(new Member("member3", 10));
        memberJpaRepository.save(new Member("member4", 10));
        memberJpaRepository.save(new Member("member5", 10));
        int age = 10;
        int offset = 0;
        int limit = 3;

        //when
        List<Member> members = memberJpaRepository.findByPage(age, offset, limit);
        long totalCount = memberJpaRepository.totalCount(age);
        // 실무중, 다음 페이지 여부나 총 페이지 갯수, 현재 페이지 위치 같은거 확인하는것 만들거면 직접 계산하고 만들어야함
        // 이게 생각보다 복잡함

        //then
        assertThat(members.size()).isEqualTo(3);
        assertThat(totalCount).isEqualTo(5);
    }

}