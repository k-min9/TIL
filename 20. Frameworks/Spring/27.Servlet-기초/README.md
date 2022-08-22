# Servelet

- 개요
자바 서블릿은 자바 언어를 사용하여 웹페이지를 동적으로 생성하는 서버 측 프로그램
요청마다 프로세스가 아닌 쓰레드로써 응답하기 때문에 가벼우며, 자바 언어로 구현된 만큼 플랫폼 종속성이 없다

- 역할
HTTP 규약에 따른 공통된 작업을 대신 수행해주고 개발자가 비즈니스 로직에만 집중할 수 있도록 도와줌

## 문법

- Controller
  - extends HttpServlet : 이미 만들어서 제공되는 추상 클래스를 상속 받아 Servlet 이 제공하는 기능들을 사용
  - @WebServlet(name="이름", urlPatterns="패턴") : Servlet 의 이름과 매핑 되는 URL 패턴을 정의하기 위한 어노테이션
  - HttpServletRequest / HttpServletResponse : 각각 HTTP 요청 / 응답에 대응
  
- 메서드
  - service : 메서드와 무관하게 요청에 응답한다. 우선권 높음.
  - doGet : GET 메서드의 요청에 대해 응답한다.
  - doPost : POST 메서드의 요청에 대해 응답한다.
  - request.getParameter("key") : http query, form input 조회
  - RequestDispatcher : 응답으로 보여줄 JSP를 선택
  - requestDispatcher.forward(req, resp) : 서버 내부 호출
    - req.setAttribute(key, value) : key에 value 담기
    - req.getAttribute(key) : key에 담긴 데이터를 가져오기
      - ex) <%=request.getAttribute("p")%> [자동으로 String으로 Casting]

## 기타

- Web Container(Servlet Container)
  - 서블릿 객체를 생성하고 관리 작업 등을 수행하면서 상호작용하며 생명주기를 관리
  - 특정 URL 이 요청되었을 때 그에 맞는 서블릿을 실행하여 응답

## JSP (Java Server Page)

- 배경
  - Servlet의 한계 : 가독성, html 실수 여지, 비지니스 로직과 출력의 혼잡
- 개요 : 한계를 극복할 템플릿 엔진으로서 JSP 등장.
  - HTML내에 자바 코드를 삽입하여 웹 서버에서 동적으로 웹 페이지를 생성하여 웹 브라우저에 돌려주는 언어.
  - HTML+Elements로 구성.
- 원리 : JSP는 Servlet으로 변환된 후 실행.
  - Servlet과 하는 일이 유사하지만 HTML 표준에 따라 작성되므로 웹 디자인하기 편리
- 특징 : JSP의 request/ response 변수에 기본적으로 HttpServletRequest/ HttpServletResponse 객체가 들어있다.
- Elements
  - Directive : <%@ 지시자 %>, import 구문 표시 등
    - ex) <%@ page import="java.util.&#42; %>
  - Scriptlet : <% 자바코드 %>, 변수선언, 제어문, 객체생성 등
  - Expression : <%= 문자열%>, 문자열, 정수, method호출 등

## Servlet과 JSP

Servlet : Java로 비지니스 로직 편하지만 HTML 작성 불편
JSP : HTML 코드 작성이 편하지만, 비지니스 로직 작성이 불편 + 속도 느림(변환)
결론 : 요청을 Servlet이 받아 비지니스 로직이 처리하고 JSP에 넘기자(Forward)
