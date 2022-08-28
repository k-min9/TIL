# JQuery

- 개요
  - JavaScript 기반의 '인기 있던' 라이브러리
  - 코드 반복과 복잡한 코드로 개발되던 기존 작업에 비해 여러 가지 효과나 이벤트를 간단한 함수의 호출만으로 쉽고 빠르게 개발이 가능 하도록 도와줌
  - 브라우저 안의 객체에 접근 및 조작하기 위한 위젯 및 API를 제공
- 특징
  - CSS 선택자가 짧고 가독성&생산성이 높음
  - 다양한 기능의 플러그인과 개발자들의 참여가 높음
  - 메소드 체인 및 묵시적 반복을 통한 코드 중복 회피
  - 크로스 브라우징 문제(브라우저 dependency) 해결 (지원 브라우저 한정)
- 적용 (파일 or CDN)
  
  ```Javascript
    <script type=“text/javascript” src=“라이브러리 경로"></script>
    내지 
    <script type=“text/javascript” src=“웹 라이브러리 경로"></script>

  ```

## 사용

- 문법
  - $(‘선택자’) : jQuery(‘선택자’)의 축약, 선택자에 해당하는 객체를 반환
    - 뒤에 .메소드()나 [index]로 객체의 메소드 및 요소에 접근
    - $(‘*’) : 모든 엘리먼트
    - $(‘p’) : 태그명이 p인 모든 엘리먼트
    - $(‘#sampleId’) : id 속성명이 sampleId인 엘리먼트 한 개
    - $(‘.sampleClassName’) : class명이 sampleClassName인 모든 엘리먼트
    - $(‘E[attr=val]’) : 값이 val 인 속성 attr 를 가지는 모든 요소
      - ex) $(‘input[type=text]’) : 문서 내의 input 태그 엘리먼트 중, type 속성값이 text인 모든 엘리먼트
      - $(‘A, B’), $(‘A.B’), $(‘A>B’) 등의 자식 표현 가능
    - $( this ) : 현재 자기자신
    - $(‘선택자:필터선택자’) : 임의 요소 추출을 위한 필터 선택자 제공
  - 메소드 : 확장집합(Wrapper Set)을 반환
    - .length() : 엘리먼트 개수를 숫자로 반환
    - .get(인덱스) : 확장 집합에서 하나 혹은 모든 엘리먼트를 반환, 역순 가능
    - .each(콜백함수) : 콜렉션 순회하며 콜백함수를 호출. this 키워드 접근이 유효.
    - .attr(‘속성명’) : 속성명에 해당하는 값 반환, 속성명 뒤에 값을 넣으면 추가하거나 수정
    - $(‘선택자’).removeAttr(‘속성명’) : 속성값이 존재하면 삭제
  - $(document).ready( function() { 함수 내용 } ); : 문서 준비(DOM 로딩)후 실행
    - $(function() { 함수내용 } ) 로 생략 가능
  - $(window).load( function() { 함수내용 } ); : 모든 외부자원까지 로딩 후 실행
  - 이벤트
    - on(‘이벤트’, function() { } ) : 바인딩
    - off(‘이벤트’) : 이벤트 핸들러 제거
    - .click, .dbclick, .mouseover(), .mouseleave()... : 객체에 해당 이벤트 바인딩
  - DOM 조작
    - $(‘HTML태그’) : createElement()와 같은 기능
      - 나중에 append(To), prepend(To), before, after 등의 조작 메소드로 처리
    - $(‘선택자’).html(‘HTML태그’) : 하위 HTML 코드를 새로운 코드로 대체
      - .text, .val도 유사하게 대체
      - .remove, .empty는 삭제
    - 탐색메소드 : children, find, next, prev, siblings, parents...
  - 기타
    - .hide, .show : 해당 엘리먼트의 display:none 속성을 제어
