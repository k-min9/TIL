package hello.itemservice.web.validation;

import hello.itemservice.web.validation.form.ItemSaveForm;
import lombok.extern.slf4j.Slf4j;
import org.springframework.validation.BindingResult;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

@Slf4j
@RestController //@RequestBody 달아주는 그거
@RequestMapping("/validation/api/items")
public class ValidationItemApiController {

    //@ModelAttribute는 필드단위로 진행되기 때문에, 바인딩 실패시 이를 기록하고 다음 단계로 넘어가, 타입 오류등이 발생해도 컨트롤러가 호출된다.
    //@RequestBody는 JSON단위로 진행되기 때문에, 바인딩 실패시 이후 단계가 정지되어 컨트롤러가 호출되지 않는다.
    @PostMapping("/add")
    public Object addItem(@RequestBody @Validated ItemSaveForm form, BindingResult bindingResult) {

        log.info("API 컨트롤러 호출");

        if (bindingResult.hasErrors()) {
            log.info("검증 오류 발생 errors={}", bindingResult);
            return bindingResult.getAllErrors();
        }

        log.info("성공 로직 실행");
        return form;
    }
}
