# Java로 배우는 자료구조

인터넷 강의 + 라이브 코딩으로 진행

IDE : 이클립스



## 기본 Base

- Java 프로그램은 하나 혹은 그 이상의 클래스로 구성되어 있음
  
  - 클래스는 대문자로 시작

- main 메서드는 프로그램 실행이 시작되는 곳

- System.in : 표준 입력



## 변수, 배열, 반복문

- 변수 : 데이터를 보관하는 장소(memory)로 사용전 선언해주어야 한다.
  
  - 적용 범위(scope)를 가짐
  
  - 타입 : premitive 타입...





## 이클립스 단축키 및 제어

단축키 변경은 Window > Preferences > General > Keys (Ctrl+Shift+L) 에서 가능

- 새로운 파일/프로젝트 만들기 : Ctrl + N

- import 누락할 경우 : Ctrl + Shift + O

- 자동완성 기능 : Ctrl + space
  
  - main : main 문 자동 완성
  
  - syso, sysout : System.out.println();
  
  - try : try-catch 문
  
  - for : 다양한 반복문

- 들여쓰기 정리 : Ctrl + i
  
  - 코드 자동 정리 : Ctrl + Shift + F

- 파일 전환 : Ctrl + E

- 실행 : Ctrl + F11

- 디버깅 : 시작(F11), 계속(F8), 한줄실행(F6), 한줄실행+내부진입(F5)

- 다음 에러로 이동 : Ctrl + ,

- 클래스 이름 선택 우클릭하고 Refactor(Alt+Shift+T) > Rename 가능

- 선택된 문자열 검색 
  
  - 전체 : Ctrl + Alt + G 
  
  - 파일 내부 : Ctrl + K

## 이클립스 설정

- 자동완성 : Window > Preferences > Java > Editor > Content Assist 메뉴에서 Auto activation triggers for Java를  
  <=$:{.@qwertyuioplkjhgfdsazxcvbnm_QWERTYUIOPLKJHGFDSAZXCVBNM
  로 변경
  
  - 개인적으로 Insertion에 'Disable insertion triggers except 'Enter'' 이거 필수

- 인코딩 UTF-8로 변경 : 기억안나면 검색창에 enco 검색해서 전부 통일
  
  1. Window > Preferences > General > Workspace에서 Text file encoding을 UTF-8로 변경
  
  2. Window > Preferences > General > Content Types에서 Text 클릭하고 Default encoding을 UTF-8로 변경하고 Update

- 기본 설치 : Help > Eclipse Marketplace
