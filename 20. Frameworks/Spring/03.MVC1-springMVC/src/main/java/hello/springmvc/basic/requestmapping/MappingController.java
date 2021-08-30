package hello.springmvc.basic.requestmapping;

import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.*;

@Slf4j
@RestController
public class MappingController {

    //이런식으로 배열 사용하여 여러 주소에 호출을 달 수도 있다.
    //@RequestMapping({"/hello-basic", "/hello-go"})
    @RequestMapping(value = "/hello-basic")
    public String helloBasic(){
        log.info("helloBasic");
        return "ok";
    }

    //상태가 맞지 않을 경우 405 반환
    @RequestMapping(value = "/mapping-get-v1", method = RequestMethod.GET)
    public String mappingGetV1(){
        log.info("매핑1");
        return "ok";
    }

    //축약 가능
    @GetMapping("/mapping-get-v2")
    public String mappingGetV2(){
        log.info("매핑2");
        return "ok";
    }

    //path variable : 그니까 url에 변수가 온다는 소리, 이 변수는 실제 파라미터로 쓸 수 있다.
    @GetMapping("/mapping/{userid}")
    public String mappingPath(@PathVariable("userid") String data){
    //public String mappingPath(@PathVariable String userid 로 생략 가능
        log.info("mappingPath userID={}", data);
        return "ok";
    }

    //path variable 다중 사용
    @GetMapping("/mapping/users/{userId}/orders/{orderId}")
    public String mappingPath(@PathVariable String userId, @PathVariable Long orderId) {
        log.info("mappingPath userId={}, orderId={}", userId, orderId);
        return "ok";
    }

    
}
