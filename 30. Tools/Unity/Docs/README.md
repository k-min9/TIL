# Unity

## 개요

게임 엔진. 가벼움이 특징.

## Getting Started

- Unity Hub : 개발 환경. 여러버전의 Unity Editor를 설치하고 관리
- 일반적 필수 구성 요소 : Assets, ProjectSettings, Packages

## Notation

- Scene(씬) : 하나의 게임 월드
  - 씬 컨트롤 버튼 : 재생 버튼 클릭시, 플레이 모드 진입 <-> 해제로 토글
  - 씬 저장 : Ctrl + S
  - 씬 선택 또는 불러오기 : 하단 Project 창에서 확인 가능
- Asset(에셋) : 개발에 사용할 모든 형태의 파일.
  - 이미지, 음악, 비디오, 3D 모델, 애니메이션 파일, 스크립트 etc...
  - Material : 텍스처(이미지) + 셰이더(최종 컬러 결정)
    - 셰이더 : 질감, 빛 반사, 굴절등 고려.
      - Albedo : 반사율, 물체 표면의 기본색을 결정
- Object(오브젝트) : 구성물, 껍데기, Holder
  - 태그 : 게임 오브젝트를 분류하고 구별하는데 사용
  - gameObject : 컴포넌트 입장에서 자신이 추가된 게임 오브젝트
  - 프리팹 : 언제든지 재사용할 수 있게 미리 만들어진 게임 오브젝트 에셋(원본)
  하이어라키창에서 프로젝트 창으로 드래그&드롭시 생성
  인스턴스에 내용 수정 후, 인스펙터 창 상단 : Overrides > Apply All 클릭
  
## 인터페이스

- 레이아웃 조절 : 우측 상단. default에서 2by3등으로 조정 가능
- 창
  - 씬 : 씬에 존재하는 오브젝트를 시각적으로 편집
    - 편집 툴 박스 : 오브젝트 편집에 사용, 단축키 QWERTY
      - Hand(카메라)
      - Translate(평행이동) : 면을 누르고 이동. X(빨), Y(초), Z(파)
      - Rotate(회전) : X(빨), Y(초), Z(파)
      - Scale(크기) : X(빨), Y(초), Z(파), 전체(회)
        - Unit : Cube 한 변의 길이. 1 Plane = 10 Unit
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
          - is Trigger 항목 체크시, 충돌을 트리거의 방아쇠로 사용 가능
  - 프로젝트 : 프로젝트에 사용할 Asset(에셋)들이 표시. 드래그 드롭 추가 기능 제공
  - 콘솔 : 로그나 에러가 표시
    - 로그 종류 : 일반(흰색), 경고(노랑), 에러(빨강)

## 컴포넌트(Component)

컴포넌트 내지 컴포지션(Composition) 패턴. 조립하는 세상.
미리 만들어진 부품을 조립하여 기능을 추가하고 완성된 오브젝트를 만드는 방식
Object [=단순한 껍데기(Holder)] + Component[스스로 동작하는(완결된) 부품]

특징 : 재사용성, 독립성(기능 추가 삭제가 쉬움)

## 메시지, 브로드 캐스팅, 이벤트 메서드

## 코딩

- 언어 : C#
- 기초 문법
  - using [namespace 이름]
  - 배열 : int[] students = new int[5];
  - Start() : 코드 실행 시발점. 대표적 유니티 이벤트 메서드
  - Update() : 한 프레임(유니티 환경 : 60FPS)마다 반복 실행
  - Debug.Log("Console 창에 보이고 싶은 메시지")
- 결과 : Console창(Ctrl+Shift+C)에서 확인
- 작성 : 프로젝트 창 왼쪽 상단 + > C# Script 클릭
  - 생성된 스크립트 더블 클릭시 VS로 넘어가서 수정 가능
- 반영
  - 저장하고 나오면 코드가 유니티에 내용 반영
  - 코드(프로젝트 창)를 오브젝트(하이어라키 창)에 드래그&드롭하여 스크립트 추가
  - 플레이 모드 시 관련 이벤트에 맞게 실행
    - 컴포넌트를 변수에 연결 : 인스펙터창에서 선언 public변수에 값을 할당

## UI

개요 : 유니티에서는 UI 요소를 게임 월드 속의 게임 오브젝트로 취급

- Text 등의 UI 제작시, 캔버스와 이벤트 시스템 게임 오브젝트가 함께 생성
  - 캔버스 : UI 요소를 표현할 2차원 평면(액자 역할). 모든 UI는 캔버스의 자식.
  - 이벤트시스템 : UI 오브젝트에 클릭, 터치, 드래그 같은 상호 작용을 이벤트 메시지로 전달

- 앵커 프리셋 : UI요소를 배치하기 위한 앵커, 피벗, 포지션값 조정용 설정창
  - Alt를 누른 상태에서는 스냅핑(앵커와 함께 포지션도 조절) 활성화

## 게임 매니저

개요 : 규칙과 상태 표현(게임 오버 유무) 및 수치 관리와 UI 갱신등을 담당

- PlayerPrefs(Player preference) : 수치를 저장하고 부를 수 있는 키-값 형태의 로컬 저장소
  - PlayerPrefs.SetFloat("key", value); 같은 GET/SET 방식
  - value로 Float, Int, String 지원

### 싱글톤 패턴

개요: 유니티에는 접근이 쉽고, 단 하나만 존재하는 관리자 역할 오브젝트가 필요함

- 정적(static) 변수를 활용 : 여러 오브젝트가 한 변수를 공유하게 설계, 클래스.연산자로 접근 가능

## 공간

- 전역 공간 : 게임 월드의 원점을 기준으로 한 좌표
- 지역 공간 : 부모 오브젝트를 원점으로 한 좌표
  - 오브젝트 공간 : 자신을 중심으로 한 좌표(편의상 지역공간과 묶음)
  - 위치, 회전, 스케일이 부모값을 따라감

## 배경음악과 효과음

- 오디오 클립을 하이어라키 창에 드래그&드롭하여 오디오 소스 컴포넌트 생성
- 일단은 생략

## Assets

- 외부 Assets을 활용하여 바퀴를 두 번 만들 필요가 없어진다.
- 구매하기 : Asset store
- 사용하기 : 창 -> window -> package manager -> My assets -> Download -> Import

## Animator

- Animation Controller로 제어, 각각 Exit, AnyState, Entry 등에 적용
  - Has Exit Time : 애니메이션 재생 종료시 Exit으로 빠져나감
  - Transition Duration : 애니메이션 적용에 필요한 시간
- 애니메이션 정보는 모델의 fbx 파일 안에 있음
  - FBX : 각종 정보들이 구분되어 저장되는 3D 포맷
- 상태를 제어할 Parameter을 좌측에서 추가
  - 방법 1 :
  애니메이션 상태 사이를 양방향 Transition으로 연결
  Parameter을 Condition으로 사용하여 연결된 Transition 완성하기
  - 방법 2 : 
  블렌더 사용하기
- parameter 변수 설정 Tip
  - float : 이동 등 강약 있음
  - Boolean : 걷는 중, 뛰는 중 같은 상태 확인
  - Trigger : 도약함 등 한번만 사용
  
## 기타

- 새로운 입력키 : Edit > Project Settings > Input Manager에서 추가 가능

- Debug.Log("내용")으로 동작확인

- 오브젝트 풀링 : 초기에 필요한 만큼 오브젝트를 미리 만들어 'Pool'에 쌓아두는 방식
  - Instantiate, Destroy 같은 처리량이 많은 로직을 조금 써서 프리징 등을 막을 수 있고, 재사용이 가능함
  - 게임 중간에 끊김이 없어지거나 감소하는 대신에 로딩시간이 길어짐
