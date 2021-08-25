package hello.core.singleton;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.*;

class StatefulServiceTest {

    @Test
    void 상태유지싱글톤(){
        ApplicationContext ac = new AnnotationConfigApplicationContext(TestConfig.class);

        StatefulService statefulService1 = ac.getBean(StatefulService.class);
        StatefulService statefulService2 = ac.getBean(StatefulService.class);

        //ThreadA 사용자 1만원 주문
        int userAprice = statefulService1.order("userA", 10000);

        //ThreadB 사용자 2만원 주문
        int userBprice = statefulService2.order("userB", 20000);

//        //ThreadA 사용자A 주문 금액 조회
//        int price = statefulService1.getPrice();
//        System.out.println("price = " + price);
//
//        //B의 2만이 저장되어있다.
//        assertThat(statefulService1.getPrice()).isEqualTo(20000);
        System.out.println("price = " + userAprice);
        System.out.println("price = " + userBprice);

    }

    static class TestConfig{

        @Bean
        public StatefulService statefulService(){
            return new StatefulService();
        }

    }

}