package hello.thymeleaf.basic;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/template")
public class TemplateController {

    //템플릿 조각 (조각도 레이아웃도 th:fragment)
    @GetMapping("fragment")
    public String template(){
        return "template/fragment/fragmentMain";
    }

    //템플릿 레이아웃 (레이아웃을 두고, 조각으로 쓸걸 미리 적극적으로 올려놓자.)
    @GetMapping("layout")
    public String layout() {
        return "template/layout/layoutMain";
    }

    //템플릿 레이아웃 확장(head가 아니고 html 전체 적용)
    @GetMapping("/layoutExtend")
    public String layoutExtend() {
        return "template/layoutExtend/layoutExtendMain";
    }


    
}
