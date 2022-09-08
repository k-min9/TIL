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

- JDK 동적 프록시 : 인터페이스 기반으로 작동 (V1 케이스에만 적용 가능)
  - InvocationHandler를 구현한 핸들러로 JDK 동적 프록시에 적용할 공통 로직 개발
  - Proxy.newProxyInstance(클래스 로더 정보, 인터페이스, 핸들러 로직) : 동적으로 프록시 객체 생성
  
    ``` Java

      AInterface proxy = (AInterface) Proxy.newProxyInstance(AInterface.class.getClassLoader(), new Class[] {AInterface.class}, handler);
      proxy.call();
    ```

- CGLIB(Code Generator Library) : 바이트 코드를 조작해 클래스를 생성하는 라이브러리
  - 인터페이스 없이 구체 클래스만으로도 동적 프록시를 생성할 수 있음
    - jdk에서 InvocationHandler를 쓰듯이 MethodInterceptor를 사용하여 invoke
  - 다만 이어지는 proxy Factory를 사용하면 편리하게 그 동작을 할 수 있으므로 이런 개념이 있다만 알고 넘어가자
  - 키워드 : Enhancer, setSuperclass, setCallback, ConcreteService

## 프록시 팩토리

스프링이 지원하는 프록시

- 배경 : JDK, CGLIB등을 상황에 따라 분리하여 적용하고 관리해야 할까?
- 개요 : 스프링은 항상 유사한 기술이 있을때 통합해서 일관성 있게 + 더 편하게 추상화된 기술을 제공
- 흐름 : adviceInvocationHandler과 adviceMethodInterceptor로 advice를 호출하면 끝
- 메소드
  - new ProxyFactory(target) : 프록시의 호출 대상을 넘기면 그 정보를 기반으로 프록시를 만들어낸다.
    - 인스턴스가 인터페이스가 있으면 jdk, 없으면 cglib 기반 동적 프록시를 생성
  - proxyFactory.addAdvice(advice) : 프록시가 사용할 부가 로직(advice) 추가
  - proxyFactory.setProxyTargetClass(true) : 인터페이스가 있어도 강제로 CGLIB 사용
    - 실무 : 기본적으로 인터페이스가 있어도 이 옵션 항상 사용함!
  - proxyFactory.getProxy() : 프록시 객체를 생성하고 반환
- 단어 정의
  - 포인트컷(Pointcut) : 어디에 부가 기능을 적용할지, 적용하지 않을지 판단하는 필터링 로직
  - 어드바이스(Advice) : 프록시가 호출하는 부가 기능이다. 프록시 로직
  - 어드바이저(Advisor) : 어디(Pointcut)에 조언(Advice)를 적용할지 알고 있는 것. 단순히 포인트컷1 + 어드바이스1
    - 이런 방식으로 역할과 책임을 명확히 분리할 수 있다.
    - 어드바이저가 여럿일 경우 1프록시에 여러 어드바이저를 적용한다.
      - 즉 스프링의 AOP는 target마다 하나의 프록시만 생성
- 예시

  ``` Java
    ServiceInterface target = new ServiceImpl();
    ProxyFactory proxyFactory = new ProxyFactory(target);

    // 스프링이 제공하는 포인트 컷 중 하나 (이름 패턴 매칭용)
    NameMatchMethodPointcut pointcut = new NameMatchMethodPointcut();
    pointcut.setMappedNames("request*", "order*", "save*");  // request*... 호출시 적용

    // Advisor 인터페이스의 가장 일반적인 구현체
    DefaultPointcutAdvisor advisor = new DefaultPointcutAdvisor(pointcut, new TimeAdvice()); 
    proxyFactory.addAdvisor(advisor);  // 어드바이스가 아닌 어드바이저를!
    ServiceInterface proxy = (ServiceInterface) proxyFactory.getProxy();
  ```

- 남은 과제
  - Config마다 설정 파일이 엄청 많다.
  - 지금까지의 방법으로는 컴포넌트 스캔(V3)에 대응할 수 없다.

## 빈 후처리기

BeanPostProcessor. 객체를 빈 생성 후, 저장소에 등록하기 전에 후 처리 작업을 함
객체를 변환하여 등록하거나 바꿔칠 수 있는 막강한 기능을 보유

- 개요 : 빈을 조작하고 변경, 메서드 호출 같은 조작까지 할 수 있는 강력한 후킹 포인트
  - 스프링 컨테이너가 등록하는, 컴포넌트 스캔 대상의 빈을 제어
  - 빈 객체를 프록시로 교체하는 것도 가능
- 방식 : BeanPostProcessor 인터페이스를 구현하고, 스프링 빈으로 등록하면 스프링이 빈 후처리기로 인식하고 동작
  - 오버라이드 가능한 메서드
    - postProcessBeforeInitialization : 객체 생성 이후에 @PostConstruct 같은 초기화가 발생하기 전에 호출
    - postProcessAfterInitialization : 객체 생성 이후에 @PostConstruct 같은 초기화가 발생한 다음에 호출
