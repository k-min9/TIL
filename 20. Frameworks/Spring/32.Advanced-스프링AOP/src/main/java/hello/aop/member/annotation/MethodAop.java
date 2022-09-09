package hello.aop.member.annotation;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Target(ElementType.METHOD)  // 메소드에 붙이는 애노테이션
@Retention(RetentionPolicy.RUNTIME)  // 애노테이션은 언제까지 유지할지
public @interface MethodAop {
    String value();  // "test value"값을 집어 넣음
}
