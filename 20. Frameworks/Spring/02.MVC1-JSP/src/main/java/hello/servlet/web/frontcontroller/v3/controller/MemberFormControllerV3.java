package hello.servlet.web.frontcontroller.v3.controller;

import hello.servlet.web.frontcontroller.ModelView;
import hello.servlet.web.frontcontroller.v3.ControllerV3;

import java.util.Map;

public class MemberFormControllerV3 implements ControllerV3 {

    @Override
    public ModelView process(Map<String, String> paramMap) {
        // 뷰의 물리적 주소가 아닌, 앞과 뒤의 공통 부분을 뺀 부분만 논리 이름으로 반환
        return new ModelView("new-form");
    }
}
