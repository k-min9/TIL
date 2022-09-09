package hello.aop.order.aop;

import org.aspectj.lang.annotation.Pointcut;

/**
 * Pointcut을 공용으로 만들어 모아두기
 * Public 설정 잊지 말고!
 * 패키지 명까지 다써야 작동함
 */
public class Pointcuts {

    //hello.aop.order 패키지와 하위 패키지
    @Pointcut("execution(* hello.aop.order..*(..))")
    public void allOrder(){} //pointcut signature

    //클래스 이름 패턴이 *Service
    @Pointcut("execution(* *..*Service.*(..))")
    public void allService(){}

    //이렇게 조합해서 만들어둘 수도 있음
    //allOrder && allService
    @Pointcut("allOrder() && allService()")
    public void orderAndService() {}

}
