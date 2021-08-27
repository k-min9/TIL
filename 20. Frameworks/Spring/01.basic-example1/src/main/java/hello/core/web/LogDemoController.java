package hello.core.web;

import hello.core.common.MyLogger;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.ObjectProvider;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.servlet.http.HttpServletRequest;

@Controller //웹 추가 학습시 스프링 인터셉터나 서블릿 필터 같은 것을 활용(이건 예제고 안배웠으니 Controller)
@RequiredArgsConstructor //의존관계 자동 주입
public class LogDemoController {

    private final LogDemoService logDemoService;
    private final ObjectProvider<MyLogger> myLoggerObjectProvider;

    @RequestMapping("log-demo") //log-demo라는 요청이 오면
    @ResponseBody //view resolver(html)를 안쓰고 문자열이나 데이터 그대로 반환(입문편)
    //HttpServletRequest : 자바에서 제공하는 고객 요청 정보를 받을 수 있게 도와줌
    public String logDemo(HttpServletRequest request){
        //request scope의 내용물 테스트할때 해결법 1 : provider의 지연 속성 이용하기
        MyLogger myLogger = myLoggerObjectProvider.getObject();
        //이 시점에서 requestURL을 set
        String requestURL = request.getRequestURL().toString();
        myLogger.setRequestURL(requestURL);

        //서비스에서도 호출해 봐야지
        myLogger.log("controller test");
        logDemoService.logic("testId");
        return "OK";
    }

}