package advanced.hello.app.v0;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Repository;

@Repository
@RequiredArgsConstructor
public class OrderRepositoryV0 {

    public void save(String itemId) {
        //저장 로직
        if ("ex".equals(itemId)) {
            throw new IllegalStateException("예외 발생!");
        }
        sleep(1000);  // 상품 저장을 하는데 걸리는 시간으로 1초 지연을 준다고 가정.
    }

    private void sleep(int millis) {
        try {
            Thread.sleep(millis);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}