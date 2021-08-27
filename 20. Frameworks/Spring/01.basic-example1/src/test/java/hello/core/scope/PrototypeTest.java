package hello.core.scope;

import org.junit.jupiter.api.Test;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Scope;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;

import static org.assertj.core.api.Assertions.assertThat;

public class PrototypeTest {

    @Test
    void PrototypeFind(){
        AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(ProtoBean.class);

        System.out.println("프로토 1 찾기");
        ProtoBean ProtoBean1 = ac.getBean(ProtoBean.class);
        System.out.println("프로토 2 찾기");
        ProtoBean ProtoBean2 = ac.getBean(ProtoBean.class);
        System.out.println("bean 1 : " + ProtoBean1);
        System.out.println("bean 2 : " + ProtoBean2);
        assertThat(ProtoBean1).isNotSameAs(ProtoBean2);

        //프로토 타입이라 close가 적용되지 않은걸 확인할 수 있다.
        ac.close();
    }

    @Scope("prototype")
     static class ProtoBean {
        @PostConstruct
        public void init(){
            System.out.println("싱글톤 빈 시작");
        }

        @PreDestroy
        public void destroy(){
            System.out.println("싱글톤 빈 종료");
        }
    }
}
