package hello.thymeleaf.basic;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

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

}
