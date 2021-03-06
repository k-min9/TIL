# Java로 배우는 자료구조

인터넷 강의 + 라이브 코딩으로 진행

IDE : 이클립스

## 기본 Base

- Java 실행 과정
  - 컴파일 과정을 통해 java 소스 코드를 실행파일로 변경
    - *.java(소스 코드)에서 .class(기계어 코드)로 변경
  - Java 실행파일을 해석할 수 있는 가상머신(JVM)이 이 파일을 해석하여 실행
  
- Java 개발 도구
  - JVM : Java 가상 머신으로, Java 실행 파일을 해석하여 실행
  - JRE(Java Runtime Environment) : Java 언어로 만들어진 프로그램을 실행시키기 위한 환경
  - JDK(Java Development Kit) : Java 언어를 이용하여 프로그램을 개발하기 위한 환경
- Java 프로그램은 하나 혹은 그 이상의 클래스로 구성되어 있음
  
  - 클래스는 대문자로 시작

- main 메서드는 프로그램 실행이 시작되는 곳

- System.in : 표준 입력

## 변수, 배열, 반복문

- 변수 : 데이터를 보관하는 장소(memory)로 사용전 선언해주어야 한다.
  
  - 적용 범위(scope)를 가짐
  
  - 타입 : premitive 타입

    - premitive 외의 모든 변수는 참조 변수
  
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

## 클래스와 객체

개요 : 서로 관련있는 데이터들을 하나의 단위로 묶어두면 편할 것이다.

- 클래스
  
  - 클래스는 결국 하나의 사용자 정의 타입이다.
  
  - 원칙 : 1클래스 1파일, 항상 대문자로 시작
  
  - 클래스의 구성요소를 필드(Field)라고 한다.
  
  - 참조 타입이니 선언 후 객체 생성을 잊지 말자. 안하면 NPE!

- 객체 : 데이터(정적 속성) + 메서드(기능, 동적 속성)

- 정리 : 객체는 구현할 대상, 클래스는 객체를 정의하고 만들기 위한 설계도 이고, 그렇게 생성된 객체 하나하나를 인스턴스라고 한다.

## 메서드와 생성자

- 클래스는 가지고 있는 데이터와 관련이 깊은 메서드들도 함께 묶을 수 있다.
  이를 통해서 코드의 응집도를 높이고 결합도를 낮출수 있다.
  
  - 응집도 : 모듈의 요소들간의 연관성 척도, 내부의 기능적인 응집 정도. 높을수록 좋음
  
  - 결합도 : 모듈이 다른 모듈에 의존하는 척도, 모듈간의 상호 결합 정도. 낮을수록 좋음

- 생성자 : 객체의 데이터 필드 값을 초기화. 클래스와 동일한 이름을 가짐

## Static

- Static : 클래스는 설계도라 그 안에 데이터를 넣을 수 없는데, 이를 가능하게 함
  
  - vs non-Static : static 멤버는 class 멤버이고, non-static 멤버는 object 멤버이다.
  
  - main 메서드가 static인 이유 :  java는 모든것이 class라서 누군가가 시작점인 main이 속한 class를 만들수가 없다.
  
  - static 메서드에서 non-static 멤버를 엑세스 할 수 없는 이유 : scope상 존재하지 않기 때문이다. 생성되지 않은 객체에 접근하라는 요구.
  
  - 다른 class에 속한 static 멤버 엑세스하는 법 : (클래스이름.메서드) 로 엑세스하자
  
  - 용도 : main 메서드, 상수(PI, System.out), 순수기능(Math.abs 같은 수학 함수)

## Visibility (접근 제어)

- 접근 제어
  
  - public : 클래스 외부에서 접근이 가능
  
  - private : 클래스 내부에서만 접근이 가능
  
  - default : 동일 패키지 내부 다른 클래스에서 접근 가능
  
  - protected : 동일 패키지의 다른 클래스와 다른 패키지의 하위클래스에서 접근 가능

- 캡슐화 : 객체가 제공해주는 메서드를 통하지 않고 데이터에 접근 못하게 설정. information hiding
  
  - getter/setter/toString...

## 상속 (Inheritance)

공통적인 부분을 빼서 묶는다. 명령어는 extends

- 장점 : 유지보수 용이, 확장성 용이, 모듈을 통한 재사용성

- parent/super/base class와 child/sub/extended class의 IS-A 관계
  
  - 부모에서 no-param 생성자가 없으면 자식에서 super 호출을 해야한다.

- 오버라이딩과 오버로딩 : 발음만 비슷한 전혀 다른 개념, 생략.

- 다향성 (Polymorphism)
  
  - 부모 타입의 변수가 서브 타입의 객체를 참조할 수 있음
    - 부모의 타입으로 자식을 생성, 참조
    - 부모의 메소드로 호출
  - 장점 : Person 배열로 Teacher과 Student 동시 관리가 가능

  ``` java
    부모클래스명 변수명 = new 자식클래스명();
    Compuer computer = new Notebook("제조사", "스펙", "사이즈");
  ```

- 동적 바인딩 : 컴파일시 호출 메소드와 실행시 호출 메소드가 유동적으로 적용

  - 이때 computer의 메소드가 Computer의 것이냐, Notebook의 것을 쓸것이냐에 따라 언어적으로 static binding과 dynamic binding으로 나뉨.
  java는 dynamic binding을 사용함. 가까운 쪽을 쓴다고 기억하면 됨.
  - Person teacher일 경우, teacher.study(); 는 에러 -> ((Teacher)teacher).study();
  (하기 전에 instanceof로 꼭 확인하지)

- 하나의 배열에 서로 다른 타입을 저장, Generic Programming이 가능

## class Object와 Wrapper class

- Object : 모든 클래스의 superclass
  - equals toString등의 자체 멤버 class 보유
    - 다만 메서드를 의도대로 사용하려면 override해야 한다.

- Wrapper class : 기본 타입의 데이터를 하나의 객체로 포장해주는 클래스
  - 배경 : Object는 모든 종류의 객체를 저장할 수 있지만 primitive type은 객체가 아니라 저장이 안됨 -> primitive type을 객체로 만들어 저장하자
  - 장점 : 데이터 타입간 변환 등 여러 기능을 넣을 수 있음
  - 기타 : Autoboxing과 Unboxing을 통해 자동으로 변환해준다.

## 추상(abstract) 클래스

- 개요 : 추상 메서드를 포함한 클래스, 객체를 만들 수 없음
  - 추상 메서드 : 선언만 있고 구현이 없는 메서드
- 인터페이스 : 추상 메서드만을 가진 추상 클래스, implements로 구현
  - 존재의의 : 다중상속이 불가능한 java에서 여러 개의 interface를 사용할 수 있다.

## Generic Programming

- 개요 : 데이터 형식에 의존하지 않고, 미리 지정하지 않는 방식으로 프로그램의 재사용성을 높이는 방식의 프로그래밍
- 구현 : < T >라는 가상 타입 parameter로 지정하고, 객체 생성 시점에서 지정
- 장점
  - 잘못된 타입이 들어오는 것을 컴파일 단계에서 방지
  - 클래스 외부에서 타입을 지정하므로 체크하거나 변환할 필요가 없음
  - 재사용성이 증가함

## 컬렉션

- 개요 : 객체를 담을 수 있는 신축성 있는 주머니
- 장점 : 자동으로 크기 조절, 명시적인 이름의 메소드 사용
- 특징 : 기본 데이터 타입 저장을 위해 Wrapper Class를 이용
- 종류
  - List : ArrayList, Vector, LinkedList
  - Set : HashSet, TreeSet
  - Map : HashMap, HashTable, TreeMap, Properties

## 리스트

- 개요 : 데이터를 순차적으로 처리하는 구조로 인덱스로 관리(주소 참조)
  - 여러 데이터를 저장하고, CRUD가 가능하며 용량에 제한이 없음
  - 객체와 null을 담을 수 있다
- 함수
  - .add(데이터) : 더하기
  - .get(인덱스)
  - .set(인덱스, 교체값) : 인덱스의 내용물 교체
  - .remove(인덱스) or .remove(데이터)

- ArrayList vs Vector
  - ArrayList는 Vector 대체를 위해 만들어져서 효율적이고 주로 사용됨
  - Vector은 다수의 thread가 충돌없이 액세스할 수 있게 Synchronize 되어 있음

## HashMap

- 개요 : 키 객체와 값 객체로 구성된 객체를 저장. 중복 불가.
- 함수
  - .put(키, 데이터)
  - .get(키)
  - .size()
  - .remove(키)
  - .keySet() : 반복

    ``` java
    for ( String key : map1.keySet() ) {
      int number = map1.get( key );
    }
    ```

## 예외 처리

- 개요 : Exception 객체를 통한 폭탄 제거
- 자주 발생하는 Exception
  - ArithmeticException : /0
  - NumberFormatException, ArrayIndexOutOfBoundsException
  - NullPointerException : null로 객체에 접근하려고 하는 경우
- 처리 방법 : try ~ catch ~ finally 를 하위부터 상위로 작성
- 예외 발생 시점에서 처리하기 애매한 경우 : 상위 메소드로 throws 활용

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
