package study.datajpa.repository;

import org.springframework.beans.factory.annotation.Value;

//인터페이스 기반 projection
public interface UsernameOnly {

    // @Value("#{target.username + ' ' + target.age}")
    // 이걸 붙이면 위 내용을 반환함, 이런걸 붙이면 Open Projection 없으면 Close Projection이라고 함
    // Open Projection은 엔티티를 다 가져와서 그걸 확인하고,
    // close projection은 이름이 정확히 일치하면 그것만 확인하는 최적화한 쿼리를 실행한다.
    String getUsername();
}
