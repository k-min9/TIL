package hello.thymeleaf.basic;

import lombok.Data;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import javax.servlet.http.HttpSession;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Controller
@RequestMapping("/basic")
public class BasicController {

    @GetMapping("text-basic")
    public String textBasic(Model model){
        //data 부분에 text 전달. 그리고 이 때 <b> 라던가는 "<"라는 메시지(HTML 엔티티) 그 자체를 보내기 때문에(HTML 이스케이프) 진해지지 않는다.
        model.addAttribute("data", "Hello Spring!");
        return "basic/text-basic";
    }


    //이스케이프 하지 않는 법(th:utext, [(...)])
    @GetMapping("text-unescaped")
    public String textUnescaped(Model model){
        model.addAttribute("data", "Hello <b>Spring!<b>");
        return "basic/text-unescaped";
    }

    //변수표기 ${user.username}, ${user['username']}, ${user.getUsername()} 정도만 기억해도 편해질 듯
    @GetMapping("/variable")
    public String variable(Model model){
        User userA = new User("userA", 10);
        User userB = new User("userB", 20);

        List<User> list = new ArrayList<>();
        list.add(userA);
        list.add(userB);

        Map<String, User> map = new HashMap<>();
        map.put("userA", userA);
        map.put("userB", userB);

        model.addAttribute("user", userA);
        model.addAttribute("users", list);
        model.addAttribute("userMap", map);

        return "basic/variable";
    }

    @Data
    static class User{
        private String username;
        private int age;

        public User(String username, int age) {
            this.username = username;
            this.age = age;
        }
    }

    //기본적인 객체 표기 ${#session} 표기 외에도, ${session.sessionData}등의 표현 가능
    @GetMapping("/basic-objects")
    public String basicObjects(HttpSession session) {
        session.setAttribute("sessionData", "Hello Session");
        return "basic/basic-objects";
    }

    @Component("helloBean")
    static class HelloBean {
        public String hello(String data) {
            return "Hello " + data;
        }
    }

    //여러 표현(날짜, 자바 8은 타임리프에 날짜표시를 위해서는 추가라이브러리(부트스트링 내포)르 써서 이렇게 보내줘야 한다.)
    @GetMapping("/date")
    public String date(Model model) {
        model.addAttribute("localDateTime", LocalDateTime.now());
        return "basic/date";
    }

    //URL 표현 @{/...}, 바인딩 포함 자세한건 html에 설명
    @GetMapping("link")
    public String link(Model model) {
        model.addAttribute("param1", "data1");
        model.addAttribute("param2", "data2");
        return "basic/link";

    }

    //리터럴 : 소스 코드상 고정값 ; 문자, 숫자, 불린, null
    //리터럴에서 문자에 관한 실수(문자를 감싸는 작은 따음표' 생략 가능 조건 = 공백 없는 연속된 문자열 = 스페이스 섞인 문장은 안됨!)
    @GetMapping("/literal")
    public String literal(Model model) {
        model.addAttribute("data", "Spring!");
        return "basic/literal";
    }














}
