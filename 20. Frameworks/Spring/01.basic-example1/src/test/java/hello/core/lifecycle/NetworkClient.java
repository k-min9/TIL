package hello.core.lifecycle;

import org.springframework.beans.factory.DisposableBean;
import org.springframework.beans.factory.InitializingBean;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;

//implements InitializingBean, DisposableBean 단점이 너무 많아서 이제는 거의 안쓰는 옛날 방법
public class NetworkClient  {

    private String url;

    public NetworkClient(){
        System.out.println("생성자 호출, url = " + url);
    }

    public void setUrl(String url) {
        this.url = url;
    }

    //서비스 시작시 호출
    public void connect(){
        System.out.println("connected : " + url);
    }

    public void call(String message){
        System.out.println("call : " + url + " message = " + message);
    }

    //서비스 종료시 호출
    public void disconnect(){
        System.out.println("close : " + url);
    }

    @PostConstruct
    public void init() {
        connect();
        call("초기화 연결 메시지");
    }

    @PreDestroy
    public void close() {
        disconnect();
    }

//    //InitializingBean은 afterPropertiesSet() 메서드로 초기화를 지원한다.
//    @Override
//    public void afterPropertiesSet() throws Exception {
//        connect();
//        call("초기화 연결 메시지");
//    }
//
//    //DisposableBean은 destroy() 메서드로 소멸을 지원한다
//    @Override
//    public void destroy() throws Exception {
//        disconnect();
//    }
}

