package hello.login.web.argumentresolver;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Target(ElementType.PARAMETER) // 파라미터에 쓸 애노테이션
@Retention(RetentionPolicy.RUNTIME) // 실제 동작할때까지 애노테이션이 남아있음
public @interface Login {
}
