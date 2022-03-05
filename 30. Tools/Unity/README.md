# Unity

## 개요

게임 엔진. 가벼움이 특징.

## Getting Started

- Unity Hub : 개발 환경
- 일반적 필수 구성 요소 : Assets, ProjectSettings, Packages

## Notation

- Scene(씬) : 하나의 게임 월드
  - 씬 컨트롤 버튼 : 재생 버튼 클릭시, 플레이 모드 진입 <-> 해제로 토글
  - 씬 저장 : Ctrl + S
  - 씬 선택 또는 불러오기 : 하단 Project 창에서 확인 가능
- Asset(에셋) : 개발에 사용할 모든 형태의 파일.
  - 이미지, 음악, 비디오, 3D 모델, 애니메이션 파일, 스크립트 etc...
  
## 인터페이스

- 레이아웃 조절 : 우측 상단. default에서 2by3등으로 조정 가능
- 창
  - 씬 : 씬에 존재하는 오브젝트를 시각적으로 편집
    - 편집 툴 박스 : 오브젝트 편집에 사용, 단축키 QWERTY
      - Hand(카메라)
      - Translate(평행이동) : 면을 누르고 이동. X(빨), Y(초), Z(파)
      - Rotate(회전) : X(빨), Y(초), Z(파)
      - Scale(크기) : X(빨), Y(초), Z(파), 전체(회)
      - Rect : UI, 2D 오브젝트 크기 조정, 3D 조정시 Z축 무시
      - Transform = Translate + Rotate + Scale
    - 씬 기즈모(Gizmo) : 씬 우측 표시 XYZ 나침반
      - 기즈모 : 개발자에게만 보이는 표시들
  - 게임 : 플레이어가 실제로 보게 될 화면, Aspect로 비율이나 해상도 조절 가능
  - Hierarchy : 현재 씬에 존재하는 모든 게임 오브젝트 표시 및 새로운 오브젝트 생성
    - Main Camera : 플레이어가 보게 될 화면
    - Directional Light : 씬에 빛을 생성
    - 3D Object 생성(+키) : Cube, Plane...
  - Inspector : 해당 Object의 정보와 Component 나열
    - Component : Object를 구성하는 다양한 부품
      - rigidbody : 해당 Object가 물리와 중력의 영향을 받음
        - Component 추가 방식 : Add component > Physics > Rigidbody
      - 기본 Component
        - Transform : 3D 공간에서의 위치(position)
        - Mesh Filter : 3D 메시 파일을 받아 오브젝트의 외곽선을 지정
        - Mesh Renderer : 메시를 따라 색을 채워 그래픽 외형을 그림
        - Box Colider : 다른 물제가 부딪힐 수 있는 그래픽 외형
  - 프로젝트 : 프로젝트에 사용할 Asset(에셋)들이 표시. 드래그 드롭 추가 기능 제공
  - 콘솔 : 로그나 에러가 표시
    - 로그 종류 : 일반(흰색), 경고(노랑), 에러(빨강)

## 컴포넌트(Component)

컴포넌트 내지 컴포지션(Composition) 패턴. 조립하는 세상.
미리 만들어진 부품을 조립하여 기능을 추가하고 완성된 오브젝트를 만드는 방식
Object [=단순한 껍데기(Holder)] + Component[스스로 동작하는(완결된) 부품]

특징 : 재사용성, 독립성(기능 추가 삭제가 쉬움)

## 메시지, 브로드캐시팅, 이벤트 메서드

## 코딩

- 언어 : C#
- 기초 문법
  - using [namespace 이름]
  - 배열 : int[] students = new int[5];
  - Start() : 코드 실행 시발점. 대표적 유니티 이벤트 메서드
  - Debug.Log("Console 창에 보이고 싶은 메시지")
- 결과 : Console창(Ctrl+Shift+C)에서 확인
- 작성 : 프로젝트 창 왼쪽 상단 + > C# Script 클릭
  - 생성된 스크립트 더블 클릭시 VS로 넘어가서 수정 가능
- 반영
  - 저장하고 나오면 코드가 유니티에 내용 반영
  - 코드(프로젝트 창)를 오브젝트(하이어라키 창)에 드래그&드롭하여 스크립트 추가
  - 플레이 모드 시 관련 이벤트에 맞게 실행
    - 컴포넌트를 변수에 연결 : 인스펙터창에서 선언 public변수에 값을 할당
