package hello.aop.order.aop;

import lombok.extern.slf4j.Slf4j;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;

@Slf4j
@Aspect
public class AspectV1 {

    /**
     * 어드바이저
     * @param joinPoint
     * @return
     * @throws Throwable
     */
    // 포인트 컷
    @Around("execution(* hello.aop.order..*(..))")
    // 어드바이스
    public Object doLog(ProceedingJoinPoint joinPoint) throws Throwable {
        log.info("[log] {}", joinPoint.getSignature());  // 조인포인트 시그네쳐 : 메소드 정보 다 찍히게
        return joinPoint.proceed();
    }



}
