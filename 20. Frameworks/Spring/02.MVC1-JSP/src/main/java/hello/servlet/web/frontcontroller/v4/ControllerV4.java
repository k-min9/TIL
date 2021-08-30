package hello.servlet.web.frontcontroller.v4;

import java.util.Map;

public interface ControllerV4 {

    /**
     *
     * @param paramMap
     * @param model
     * @return viewName
     */
    //반환이 String(View name)으로 변경, map 외에 모델도 보냄
    String process(Map<String,String> paramMap, Map<String, Object> model);
}
