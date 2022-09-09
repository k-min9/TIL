package hello.aop.order.aop;

import lombok.extern.slf4j.Slf4j;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Pointcut;

@Slf4j
@Aspect
public class AspectV2 {


    /**
     * 포인트컷 분리 : 포인트컷 시그네쳐를 만듬
     * 이 예시에서는 주문과 관련된 모든 기능을 대상으로 하는 포인트 컷 allOrder를 만들었다.
      */
    // 포인트 컷(hello.aop.order 패키지와 하위 패키지)
    @Pointcut("execution(* hello.aop.order..*(..))")
    private void allOrder(){} //pointcut signature



    @Around("allOrder()")
    // 어드바이스
    public Object doLog(ProceedingJoinPoint joinPoint) throws Throwable {
        log.info("[log] {}", joinPoint.getSignature());  // 조인포인트 시그네쳐 : 메소드 정보 다 찍히게
        return joinPoint.proceed();
    }



}
