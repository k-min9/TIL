package hello.servlet.domain.member;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

//실무에서는 동시성 문제를 고려하여, ConcurrentHashMap, AtomicLong 사용을 고려해야한다.
public class MemberRepository {
    
    //스프링에서는 싱글톤이니 static 없어도 정상 동작함
    private static Map<Long, Member> store = new HashMap<>(); //static 사용
    private static long sequence = 0L; //static 사용
    private static final MemberRepository instance = new MemberRepository();
    public static MemberRepository getInstance() {
        return instance;
    }
    private MemberRepository() {
    }
    
    public Member save(Member member) {
        member.setId(++sequence);
        store.put(member.getId(), member);
        return member;
    }
    
    public Member findById(Long id) {
        return store.get(id);
    }
    
    public List<Member> findAll() {
        //store 내용 건드리고 싶지 않으니 new 선언
        return new ArrayList<>(store.values());
    }
    
    public void clearStore() {
        store.clear();
    }
}
