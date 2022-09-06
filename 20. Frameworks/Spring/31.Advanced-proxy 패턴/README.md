# 프록시 패턴과 데코레이터 패턴

크게 세가지로 나뉘는 프록시 패턴을 전부 구현해보자
v1 - 인터페이스와 구현 클래스 - 스프링 빈으로 수동 등록
v2 - 인터페이스 없는 구체 클래스 - 스프링 빈으로 수동 등록
v3 - 컴포넌트 스캔으로 스프링 빈 자동 등록

## V1, V2, V3

- V1, V2 : 다른 버전도 있으므로, 컴포넌트 스캔 대상을 축소하고 @Import로 직접 전용 Config 클래스를 등록하였다
- V3 : 친숙한 구현

## 프록시 패턴

- 배경 및 조건
  - V1, V2, V3 각각의 다양한 케이스에서 원본 코드를 전혀 수정하지 않고, 로그 추적기를 도입해보자.
  - 특정 메서드는 로그 추적기를 출력하지 않게 하자.
- 호출의 종류
  - 직접 호출 : 클라이언트가 서버를 직접 호출하고 처리결과를 직접 받음
  - 간접 호출 : 클라이언트와 서버 사이에 대리자를 두고 부탁하는 방식
    - 대리자(프록시) 사용시 여러가지 기능을 추가로 해줄 수 있다.
      - 접근 제어, 캐싱
      - 부가 기능 추가
      - 프록시 간 체인
- 프록시 객체 조건
  - 클라이언트는 프록시에 요청한지, 서버에 요청한지 몰라야 한다.
    - 클라이언트가 서버인터페이스를 사용하고, Proxy와 Server 구현체가 구현하는 방식
    - (= 같은 인터페이스를 사용해야 함)
  - 서버 객체를 프록시 객체로 변경해도 클라이언트 코드를 변경하지 않아야 한다.
    - DI를 통한 주입
- 프록시 사용 패턴 분류 : 사용 의도에 따라 분류 (생긴게 유사해도 의도로 구분)
  - 프록시 패턴 : 접근 제어가 목적
    - 권한에 따른 접근 차단
    - 캐싱 : 데이터가 이미 있다고 반환하고, 서버에 요청하지 않음
    - 지연 로딩 : proxy를 가져다가 사용하다가, 실제 요청이 있을때 조회
  - 데코레이터 패턴 : 새로운 기능 추가가 목적
    - 원래 서버가 제공하는 기능에 부가 기능을 추가
- 예시 (proxy 삽입 비교)

  ``` Java
    void noProxy() {
        ConcreteLogic concreteLogic = new ConcreteLogic();
        ConcreteClient client = new ConcreteClient(concreteLogic);
        client.execute();
    }

    void addProxy() {
        ConcreteLogic concreteLogic = new ConcreteLogic();
        // 이 부분이 proxy. 원하면 체인도 가능
        TimeProxy timeProxy = new TimeProxy(concreteLogic);
        ConcreteClient client = new ConcreteClient(timeProxy);
        client.execute();
    }
  ```

- 문제점
  - 호출대상인 component를 가지고 있어야하며, 항상 호출해야되는데 그 부분이 중복
  - 클래스가 100개면 100개의 프록시 클래스가 필요함
    - 이걸 해결 하는게 동적 프록시

## 동적 프록시

자바가 기본으로 제공하는 JDK 동적 프록시 기술이나 CGLIB 같은 프록시 생성 오픈소스 기술을 활용하면 프록시 객체를 동적으로 만들어낼 수 있다.

- 리플렉션 : 클래스나 메서드의 메타정보를 동적으로 획득하고, 코드도 동적으로 호출할 수
있게 해주는 기술

  ``` Java

  //클래스 정보
  Class classHello = Class.forName("hello.proxy.jdkdynamic.reflectionTest$Hello");
  Hello target = new Hello();

  //메서드 callA 정보
  Method methodCallA = classHello.getMethod("callA");
  Object result1 = methodCallA.invoke(target);
  ```

  - 다만 컴파일 에러가 아닌 런타임 에러가 발생하니 정말 필요할때만 쓰자

- JDK 동적 프록시 : 인터페이스 기반으로 작동
  - InvocationHandler를 구현한 핸들러로 JDK 동적 프록시에 적용할 공통 로직 개발
  - Proxy.newProxyInstance(클래스 로더 정보, 인터페이스, 핸들러 로직) : 동적으로 프록시 객체 생성
  
    ``` Java

      AInterface proxy = (AInterface) Proxy.newProxyInstance(AInterface.class.getClassLoader(), new Class[] {AInterface.class}, handler);
      proxy.call();
    ```

