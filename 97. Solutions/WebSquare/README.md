# 웹스퀘어

- 개요 : 티맥스에서 만든 프론트 프레임워크

## 구조

- XML : 특수 목적을 위해 사용하는 다목적 언어
- WebContent 폴더 : client단 서버 구축

- Property 창 구성
  - Design : Body 태그 영역에 해당
    - 좌측 Palette(검색 기능 있음)을 활용하여 Component 추가
  - Script : 비지니스 로직을 만드는 영역
    - 초기 함수 onpageload, onpageunload 삭제하지 말 것
    - ex) onpageload : 페이지 로딩 후 실행. init과 비슷한 기능
  - DataCollection : - 데이터 객체들을 정의하는 영역
    - 서버 통신을 위한 request, response 데이터와 화면에서 사용할 데이터를 정의
    - 타입 : DataMap, DataList, LinkedDataList, AliasDataMap, AliasDataList
      - Datamap : 단일 값
      - DataList : 항목이 여럿
      - LinkedDataList : 데이터 재활용에 유용
      - AliasDataMap : 부모 창에서 쓰는 데이터를 쓰고 싶을때 활용
  - Submission : 서버 통신을 위한 인터페이스
    - 동기/비동기, 함수 정의, 데이터 세팅가능
  - Source : 어떻게 구성되어 있는지 확인하는 용도정도로만 사용하자
- Outline view : 전체 화면 구조 확인에 유용
  - Design : 전체 컴포넌트 구조
  - Script : 생성된 function 및 Event
  - Head : Design, Script를 제외한 부분. DataCollection 및 Submission, 외부 css 및 js 파일

## 제어

- 컴포넌트 제어
  - 1. 속성 : 정적으로 사용할 때, 주어진 속성을 제어
  - 2. 이벤트 : 동작(onClick, onFocus)을 부여하고, 스크립트 제어
        - 이벤트 부여시 빨간 태그가 보임(id-키 필요)
  - 3. API : 스크립트에서 동적으로 제어
        - id, class 등의 항목 구분용 키 필요
- 스타일 제어
  - 직접 스타일 항목 찾고 변경
  - 속성 하단의 스타일에서 직접 작성 (자동완성 제공)
  - 인라인 : Outline에 <>버튼에 스타일 시트 추가 후 직접 입력
  - 익스터널 : 외부파일을 클릭하고 Design의 빈 공간에 드래그(외부 파일 임포트 전부 비슷) 후 id, class에 맞게 설정
- 목록성 컴포넌트 제어
  - 1. 하드코딩
  - 2. 스크립트에서 동적으로 만들기
  - 3. DataCollection
- 설정파일 : Config.xml

## 그리드 뷰

- 개요 : 대량의 데이터를 처리할 때 사용
- 그리드 뷰에 dataList 연결하고 들어갈 column에 ID 넣자
  - dataList째 데이터뷰에 옮기기도 가능

## 단축키

- F1 : help, 컴포넌트 선택상태에서 사용시 컴포넌트 용 도움말이 나옴
- F7 : 로컬 실행  
  - 화면에서 Ctrl + 우클릭 : 디버깅 콘솔
  (개발 끝나고 운영에서는 debugMenu block으로 고쳐두자)
