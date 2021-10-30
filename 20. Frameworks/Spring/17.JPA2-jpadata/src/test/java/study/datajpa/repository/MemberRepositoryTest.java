package study.datajpa.repository;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestMethodOrder;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Slice;
import org.springframework.data.domain.Sort;
import org.springframework.test.annotation.Rollback;
import org.springframework.transaction.annotation.Transactional;
import study.datajpa.dto.MemberDto;
import study.datajpa.entity.Member;
import study.datajpa.entity.Team;

import java.util.Arrays;
import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
@Transactional  // org. // 모든 데이터 변경은 Transactional 내부에서 일어나니까 필수
@Rollback(false)  // 이거 해둬야 롤백 안하고 DB에 결과가 남아서 내용 볼 수 있음
class MemberRepositoryTest {

    @Autowired
    MemberRepository memberRepository;
    @Autowired
    TeamRepository teamRepository;

    @Test
    public void testMember(){
        Member member = new Member("memberA");
        Member savedmember = memberRepository.save(member);

        Member findmember = memberRepository.findById(savedmember.getId()).get(); // get 실제로는 nosuchelement에러 뜰 수 있으니 따로 해야함

        assertThat(findmember.getId()).isEqualTo(member.getId());
        assertThat(findmember.getUsername()).isEqualTo(member.getUsername());
        assertThat(findmember).isEqualTo(member);
    }

    @Test
    public void testQuery() {
        Member m1 = new Member("AAA", 10);
        Member m2 = new Member("BBB", 20);
        memberRepository.save(m1);
        memberRepository.save(m2);

        List<String> usernameList = memberRepository.findUsernameList();
        for (String s : usernameList){
            System.out.println("s = " + s);
        }
    }

    @Test
    public void findMemberDto() {
        Team team = new Team("teamA");
        teamRepository.save(team);


        Member m1 = new Member("AAA", 10);
        m1.setTeam(team);
        memberRepository.save(m1);

        List<MemberDto> memberDto = memberRepository.findMemberDto();
        for (MemberDto dto : memberDto){
            System.out.println("dto = " + dto);
        }

    }

    @Test
    public void findByNames() {
        Member m1 = new Member("AAA", 10);
        Member m2 = new Member("BBB", 20);
        memberRepository.save(m1);
        memberRepository.save(m2);

        List<Member> result = memberRepository.findByNames(Arrays.asList("AAA", "BBB"));
        for (Member member : result) {
            System.out.println("member = " + member);
        }

    }

    @Test
    public void paging() throws Exception {
        //given
        memberRepository.save(new Member("member1", 10));
        memberRepository.save(new Member("member2", 10));
        memberRepository.save(new Member("member3", 10));
        memberRepository.save(new Member("member4", 10));
        memberRepository.save(new Member("member5", 10));
        int age = 10;
        int offset = 0;
        int limit = 3;

        // 0페이지(스프링 데이터는 0부터 시작작)부터 시작해 3개 가져와
        PageRequest pageRequest = PageRequest.of(0, 3, Sort.by(Sort.Direction.DESC, "username"));

        //when
        Page<Member> page = memberRepository.findByAge(age, pageRequest);

        //then
        List<Member> content = page.getContent();  // 이러면 싹 가져옴
        long totalElements = page.getTotalElements();

//        for (Member member : content) {
//            System.out.println("member = " + member);
//        }
//        // 반환타입을 Page로 작업시 totalCount 같은것도 알아서 계산해 줌 (알아서 토탈 쿼리 날림)
//        System.out.println("totalElements = " + totalElements);

        //assertThat으로 test
        assertThat(content.size()).isEqualTo(3);  // 리스트 안에 갯수
        assertThat(page.getTotalElements()).isEqualTo(5);  // 총 갯수
        assertThat(page.getNumber()).isEqualTo(0);  // 페이지 번호 (계산이 필요없는 스프링 데이터의 편의점!)
        assertThat(page.getTotalPages()).isEqualTo(2);  // 총 페이지 수 (3개+2개로 2페이지 나옴)
        assertThat(page.isFirst()).isTrue();  // 첫 번째 페이지냐
        assertThat(page.hasNext()).isTrue();  // 다음 페이지 있냐

    }

    @Test
    public void pagingSlice() throws Exception {
        //given
        memberRepository.save(new Member("member1", 10));
        memberRepository.save(new Member("member2", 10));
        memberRepository.save(new Member("member3", 10));
        memberRepository.save(new Member("member4", 10));
        memberRepository.save(new Member("member5", 10));
        int age = 10;
        int offset = 0;
        int limit = 3;

        // 0페이지(스프링 데이터는 0부터 시작작)부터 시작해 3개 가져와
        PageRequest pageRequest = PageRequest.of(0, 3, Sort.by(Sort.Direction.DESC, "username"));

        //when
        Slice<Member> page = memberRepository.findSliceByAge(age, pageRequest);

        //then
        List<Member> content = page.getContent();  // 이러면 싹 가져옴

        assertThat(content.size()).isEqualTo(3);  // 리스트 안에 갯수
        //assertThat(page.getTotalElements()).isEqualTo(5);  // 총 갯수
        assertThat(page.getNumber()).isEqualTo(0);  // 페이지 번호 (계산이 필요없는 스프링 데이터의 편의점!)
        //assertThat(page.getTotalPages()).isEqualTo(2);  // 총 페이지 수 (3개+2개로 2페이지 나옴)
        assertThat(page.isFirst()).isTrue();  // 첫 번째 페이지냐
        assertThat(page.hasNext()).isTrue();  // 다음 페이지 있냐


        /** 실무 꿀 팁!!!*/
        //활용 2편 생각하면 알겠지만 API에서 엔티티를 직접 반환하면 안된다 -> DTO 변환씨의 꿀팁 = map
        Slice<MemberDto> memberDtos = page.map(member -> new MemberDto(member.getId(), member.getUsername(), null));

    }
}