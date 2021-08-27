package hello.core.common;

import org.springframework.context.annotation.Scope;
import org.springframework.context.annotation.ScopedProxyMode;
import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;
import java.util.UUID;

@Component
@Scope(value = "request")//, proxyMode = ScopedProxyMode.TARGET_CLASS) >> 프록시로 request 빈을 처리한다.
public class MyLogger {

    private String uuid;
    private String requestURL; // 외부에서 요청들어올때 setter로 입력받는다.

    public void setRequestURL(String requestURL) {
        this.requestURL = requestURL;
    }

    public void log(String message){
        System.out.println("[" + uuid + "][" + requestURL + "]" + message);
    }

    @PostConstruct
    public void init(){
        //http 생성시에 생기고, 다른 http 요청과 구분하는데 사용
        //로또의 로또의 로또의 로또가 당첨될 확률로 안겹침
        uuid = UUID.randomUUID().toString();
        System.out.println("UUID : " + uuid + "가 만들어짐" + this);
    }

    @PreDestroy
    public void close() {
        System.out.println("UUID : " + uuid + "가 종료됨" + this);
    }
}
