package hello.login.web.interceptor;

import lombok.extern.slf4j.Slf4j;
import org.springframework.web.method.HandlerMethod;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.UUID;

@Slf4j
public class LogInterceptor implements HandlerInterceptor {

    //싱글톤이니까 여기에 변수(UUID라던가) 설정하면 안된다ㅡ 상수 only
    public static final String LOG_ID = "logid";


    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        String requestURI = request.getRequestURI();
        String uuid = UUID.randomUUID().toString();

        //변수로 하지 말고 request에 넣어라~
        request.setAttribute(LOG_ID, uuid);

        //사용하는 핸들러 매핑에 따라 넘어오는 핸들러가 다르다.
        //@RequestMapping: HandlerMethod
        //정적 리소스: ResourceHttpRequestHandler
        if (handler instanceof HandlerMethod) {
            HandlerMethod hm = (HandlerMethod) handler;//호출할 컨트롤러 메서드의 모든 정보가 포함되어 있다.(그래서 기본값 Object)
        }

        log.info("REQUEST [{}][{}][{}]", uuid, requestURI, handler);
        return true; //false시 거기서 끝남, true는 다음 동작(컨트롤러 호출) 수행
    }

    //컨트롤러 오류시 실행되지 않음
    @Override
    public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception {
        log.info("postHandle [{}]", modelAndView);
    }

    //컨트롤러 오류 여부에 상관없이 무조건 실행
    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {
        String requestURI = request.getRequestURI();
        String logId = (String) request.getAttribute(LOG_ID);

        log.info("RESPONSE [{}][{}][{}]", logId, requestURI, handler);
        //예외가 터졌으면 이게 null이 아니겠지?
        if (ex != null) {
            log.error("afterCompletion error!!", ex);
        }
    }
}
