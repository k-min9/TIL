package hello.servlet.web.frontcontroller.v5;

import hello.servlet.web.frontcontroller.ModelView;
import hello.servlet.web.frontcontroller.MyView;
import hello.servlet.web.frontcontroller.v3.ControllerV3;
import hello.servlet.web.frontcontroller.v3.controller.MemberFormControllerV3;
import hello.servlet.web.frontcontroller.v3.controller.MemberListControllerV3;
import hello.servlet.web.frontcontroller.v3.controller.MemberSaveControllerV3;
import hello.servlet.web.frontcontroller.v4.ControllerV4;
import hello.servlet.web.frontcontroller.v4.controller.MemberFormControllerV4;
import hello.servlet.web.frontcontroller.v4.controller.MemberListControllerV4;
import hello.servlet.web.frontcontroller.v4.controller.MemberSaveControllerV4;
import hello.servlet.web.frontcontroller.v5.adapter.ControllerV3HandlerAdapter;
import hello.servlet.web.frontcontroller.v5.adapter.ControllerV4HandlerAdapter;
import org.springframework.web.servlet.HandlerAdapter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@WebServlet(name = "frontControllerServletV5", urlPatterns = "/front-controller/v5/*")
public class FrontControllerServletV5 extends HttpServlet {
    @Override
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        //0. 일단 V3 컨트롤러 버전 다 가져옴 >> 변형 및 extract method

        //1. 핸들러 찾아와
        Object handler = getHandler(request);

        if (handler == null) {
            response.setStatus(HttpServletResponse.SC_NOT_FOUND);
            return;
        }

        //2. 핸들러 어댑터 찾아와
        //핸들러 어댑터 목록에서 핸들러를 찾아와야한다. >> 루프 사용
        MyHandlerAdapter adapter = getHandlerAdapter(handler);

        //3. 어댑터에 리퀘스트, 리스폰스, 핸들러 다 넣으면 모델뷰를 반환 함
        ModelView mv = adapter.handle(request, response, handler);

        String viewName = mv.getViewName(); // 논리이름 챙겨오기
        MyView view = viewResolver(viewName);

        //이제부턴 렌더링할 때 모델을 함께 넘겨야 한다.
        view.render(mv.getModel(), request, response);
    }

    private Object getHandler(HttpServletRequest request) {
        String requestURI = request.getRequestURI();
        return handlerMappingMap.get(requestURI);
    }

    private MyHandlerAdapter getHandlerAdapter(Object handler) {
        for (MyHandlerAdapter adapter : handlerAdapters) {
            // 아까 그 핸들러 종류 보고 어댑터 필요 여부 반환하던 인터페이스의 그거
            if (adapter.supports(handler)){
                return adapter;
            }
        }
        throw new IllegalArgumentException("handler adapter를 찾을 수 없습니다.");
    }

    private MyView viewResolver(String viewName) {
        return new MyView("/WEB-INF/views/" + viewName + ".jsp");
    }



    //V4 버전
//    private Map<String, ControllerV4> controllerMap = new HashMap<>();
    //V5 버전 : 어떤 컨트롤러도 들어갈 수 있게 Object로 바꾸었다.
    private final Map<String, Object> handlerMappingMap = new HashMap<>();
    //어댑터가 여럿 담겨 있고 그중에 하나를 꺼내 써야 되기 때문에 하나 더 추가해야한다.
    private final List<MyHandlerAdapter> handlerAdapters = new ArrayList<>();

    //위에 handlerMappingMap, handlerAdapters에 값을 넣어 줘야지
    public FrontControllerServletV5() {

        //생성자로 초기 핸들러매핑정보와 핸들러어댑터 목록 등록
        InitHandlerMappingMap();
        InitHandlerAdapters();
    }

    //일단 V3버전 리팩토링
    private void InitHandlerMappingMap() {
        // 주소가 이상해보이지만 v5의 하위인 v3로 읽어야 된다.
        handlerMappingMap.put("/front-controller/v5/v3/members/new-form", new MemberFormControllerV3());
        handlerMappingMap.put("/front-controller/v5/v3/members/save", new MemberSaveControllerV3());
        handlerMappingMap.put("/front-controller/v5/v3/members", new MemberListControllerV3());

        //V4 추가
        handlerMappingMap.put("/front-controller/v5/v4/members/new-form", new MemberFormControllerV4());
        handlerMappingMap.put("/front-controller/v5/v4/members/save", new MemberSaveControllerV4());
        handlerMappingMap.put("/front-controller/v5/v4/members", new MemberListControllerV4());
    }

    private void InitHandlerAdapters() {
        handlerAdapters.add(new ControllerV3HandlerAdapter());
        handlerAdapters.add(new ControllerV4HandlerAdapter());
    }

}
