package hello.servlet.web.frontcontroller.v5.adapter;

import hello.servlet.web.frontcontroller.ModelView;
import hello.servlet.web.frontcontroller.v4.ControllerV4;
import hello.servlet.web.frontcontroller.v5.MyHandlerAdapter;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.HashMap;
import java.util.Map;

public class ControllerV4HandlerAdapter implements MyHandlerAdapter {

    //handler가 controllerV4일때만 처리
    @Override
    public boolean supports(Object handler) {
        return (handler instanceof ControllerV4);
    }

    @Override
    public ModelView handle(HttpServletRequest request, HttpServletResponse response, Object handler) {

        //handler를 V4로 casting
        ControllerV4 controller = (ControllerV4) handler;

        //해당 컨트롤러 호출
        Map<String, String> paramMap = createParamMap(request);
        Map<String, Object> model = new HashMap<>();

        //viewname 반환받기
        String viewName = controller.process(paramMap, model);

        //controllerv4가 뷰의 이름을 반환했지만 어댑터는 이걸 modelview 형식으로 만들어서 반환한다. 말그대로 어댑터
        ModelView mv =new ModelView(viewName);
        mv.setModel(model);

        return mv;
    }

    private Map<String, String> createParamMap(HttpServletRequest request) {
        Map<String, String> paramMap = new HashMap<>();
        request.getParameterNames().asIterator()
                .forEachRemaining(paramName -> paramMap.put(paramName, request.getParameter(paramName)));
        return paramMap;
    }
}