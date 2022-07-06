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
  
  - 문자열은 premitive 타입이 아니기 때문에 == 로 비교할 수 없다. 
    .equals 쓰자

- 배열 : 동일한 형태의 변수 여러개를 저장할 수 있는 특별한 형태의 변수

## 메서드 호출과 프로그램의 기능적 분할

- 메서드 : 함수

- java는 call by value(값에 의한 호출) 밖에 할 수 없다. 
  
  - java는 call by ref(참조에 의한 호출) 불가

- 클래스 전체에서 사용될 데이터는 static하게 클래스의 멤버로 만드는 것이 좋다.

## 문자열 다루기

- 대표적인 데이터의 형태인 문자열을 제어하기 위한 방법을 알아보자

- 기본 메서드
  
  - equals, compareTo, length, charAt(2), indexOf('b'), substring

- 기타
  
  - isLetter, toLowerCase, trim < strip (탭이나 스페이스 외에도 제거)



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

- 에러 발생시 왼쪽의 빨간색 클릭하면 적절한 대응을 소개해 줌

## 이클립스 설정

- 자동완성 : Window > Preferences > Java > Editor > Content Assist 메뉴에서 Auto activation triggers for Java를  
  <=$:{.@qwertyuioplkjhgfdsazxcvbnm_QWERTYUIOPLKJHGFDSAZXCVBNM
  로 변경
  
  - 개인적으로 Insertion에 'Disable insertion triggers except 'Enter'' 이거 필수

- 인코딩 UTF-8로 변경 : 기억안나면 검색창에 enco 검색해서 전부 통일
  
  1. Window > Preferences > General > Workspace에서 Text file encoding을 UTF-8로 변경
  
  2. Window > Preferences > General > Content Types에서 Text 클릭하고 Default encoding을 UTF-8로 변경하고 Update

- 기본 설치 : Help > Eclipse Marketplace
