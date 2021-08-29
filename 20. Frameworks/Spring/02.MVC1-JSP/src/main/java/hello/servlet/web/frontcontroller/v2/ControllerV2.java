package hello.servlet.web.frontcontroller.v2;

import hello.servlet.web.frontcontroller.MyView;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public interface ControllerV2 {

    //v1과의 차이 : 반환이 void 에서 MyView로 바뀜
    MyView process(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException;
}
