package study.datajpa.repository;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.annotation.Rollback;
import org.springframework.transaction.annotation.Transactional;
import study.datajpa.entity.Member;

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

}