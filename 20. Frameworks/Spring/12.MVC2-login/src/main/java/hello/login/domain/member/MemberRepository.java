package hello.login.domain.member;

import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Repository;

import java.util.*;

//저장소를 바꿀 수 있는 인터페이스 구현이 더 좋지만, 일단 예제니까 직접 구현
@Slf4j
@Repository // 저장소라는 시멘틱한 표현의 @Controller
public class MemberRepository {

    //static으로 의존성 신경 안쓰고 일단은 진행
    private static Map<Long, Member> store = new HashMap<>();
    private static long sequence = 0L;

    public Member save(Member member){
        member.setId(++sequence);
        log.info("저장 : member = {}", member);
        store.put(member.getId(), member);
        return member;
    }

    public Member findById(Long id) {
        return store.get(id);
    }

    //로그인 아이디 찾기, 못 찾을 수도 있으니 Optional
    public Optional<Member> findByLoginId(String loginId){
//        List<Member> all = findAll();
//        for (Member m : all){
//            if(m.getLoginId().equals(loginId)){
//                return Optional.of(m); // return m의 optional 버전 문법
//            }
//        }
//        return Optional.empty();

        //위 로직의 람다식 버전 >> 람다식 공부해라
       return findAll().stream() // stream : 대충 루프 도는 것과 비슷
                .filter(m -> m.getLoginId().equals(loginId)) // filter로 조건 만족되는것 찾기
                .findFirst(); //filter로 걸러진 것중 가장 먼저 발견한것
    }

    public List<Member> findAll(){
        return new ArrayList<>(store.values());
    }

    public void clearStore() {
        store.clear();
    }

}
