# MSA (Micro Service Architecture)

- 개요 : 여러 작은 서비스들로 구성된, 서비스의 집합인 Application을 개발
- 배경 : 모놀릭 통합 빌드/배포로 추가/변경 요구사항 대응이 점점 어려워짐
- 모놀릭(Monolithic)과의 차이점으로 보는 장단점
  - 기존 : 모든 구성요소들이 하나의 Application에 통합 개발되어 빌드 되고 배포하는 설계
  - 장점 : 장애격리, 독립무중단배포, DB분리, 작은 서비스 단위 개발
    - 논리적 분리의 한계를 물리적 분리로 극복 > 복잡도 감소
    - 대규모 개발자에 의한 개발/유지보수가 용이해짐
    - 업무별 배포와 확장이 쉽고 편해지며 장애 격리에 유리함
    - 다양한 사업환경 변화 대응에 좋음(Agility, Rapid, Frequent, Reliable)
    - Cloud-native라 Auto Scaling, 보안, Api Gateway, Monitoring 등 부가 기능 활용이 용이
  - 단점
    - MSA 도입을 위한 추가 설계, 기반 기술, 조직 재정비 등의 Cost가 필요
      - 도입은 신중히!
    - 메시지의 네트워크 전송시간 등의 오버헤드 발생
    - 테스팅 복잡도 증가.
    - 트랜잭션을 묶기가 어려움
      - 메시징 큐 도입 등 의 별도 방안으로 해결 가능함
      - 이 외에도 분산 데이터 조회, 모니터링, 호출 추적이 어렵지만 별도 방안으로 해결 가능(Cost 증가)
- 용어
  - IPC : Inter-Process Communication, 프로세스간 통신.

## 분산 트랜잭션

- 배경
  - 서비스별 DB가 분리되어있는데 기존 트랜잭션 방법으로 가능할까
  - 여러 서비스 DB간 일관성을 유지해야 하는데, 특정 서비스에서 장애가 발생하면?
  - 기존의 ACID 대안으로 BASE 가 필요함
    - ACID : 원자성, 일관성, 독립성, 지속성
    - BASE
      - BA(Basically Available) : 가용성 중시/우선
      - S(Soft-State) : 외부로 부터 받은 정보를 업데이트하는 Soft-state
        - 노드의 상태(DB 상태값)은 내부 정보가 아닌 외부 전송 정보로 결정
      - E(Eventually Consistency) : 실시간은 아니어도 최종적으로 일관성이 유지되면 됨
        - 재호출, 분산 트랜잭션
- 요구사항 : 데이터 정합성
  - 프로세스나 데이터 분산에 따른 복잡성 상승
  - 대기 또는 실패시 재호출
  - 보상 트랜잭션 처리(Saga등의 패턴 적용 등으로 구현 가능)
- 보상 트랜잭션
  - 기존의 트랜잭션 무효화 방법인 Undo/Rollback의 대안
  - 순방향 트랜잭션의 역방향으로 실행할 트랜잭션을 구축하여 최종적으로 정합성이 맞게 설계(Eventually Consistency)
- Saga Pattern : 각 서비스 하위의 Local Tx가 존재하고 그 Local Tx들을 연결한 집합체가 존재
  - Long Lived Transactions으로 기존 방식에 비해 복잡성이 증가하므로, 다른 문제가 없을지 고려해야 함
  - 종류
    - Orchestration : Command 기반, 로직을 중앙(Orchestrator)에서 통제, 타서비스 Local Tx를 호출하여 Business Logic을 구성
      - 기존의 방식과 유사하여 이해가 쉬우나 중앙을 위한 추가 서비스가 필요할 수 있고 결합도가 높아짐
    - Cheography : Event 기반, 별도의 조정자가 없음, 각 Local Tx가 완료되면 이벤트를 Publish하여 타 Local Tx가 실행되도록 함
      - 결합도가 낮고 타 서비스의 로직을 알 필요 없이, 서비스별 분산이 되어 있음.
      - Event 주고받는 서비스들간의 순환적 종속성(Cyclic Dependencies) 증가
      - 이벤트간 추적이 어렵고, 처리 Step이 변경될 때, 혼란스러울 수 있음
- 분산 데이터 조회
  - API Composition : 여러 서비스 API 호출 결과를 조합하여 Response
    - 여러 서비스 API를 병렬로 호출하고, 그 결과를 조합
    - 대량이나 복잡한 데이터에는 적합하지 않음
  - CQRS(Command Query Responsibility Segregation) : Command(저장)과 Query(조회)의 책임을 분리하는 패턴
    - 저장 완료 후, 해당 내용을 event로 조회용 DB에 저장 -> 조회시 타 API를 호출할 필요가 없어짐
    - 기존의 서비스가 조회/통계때문에 복잡해지는 것을 방지하여 모델이 단순해지고, 저장이 달라지니 적용 기술을 분리할 수 있음
      - 필요한 데이터가 다르니 아예 독립적 서비스(Standalone Service) 구축 가능
    - 대량 데이터 서비스간의 빈번한 RoundTrip, MSA DB 분리에 따른 Join 한계 등을 개선할 수 있음 > 성능 향상 기대
      - Roundtrip : 클라이언트-서버 간의 데어터 왕복 과정. 빈번하다 = 서버 쪽 부담이 크고 성능에 악영향.
    - 영향도 파악, 추적, 디버깅이 어려움

## 아키텍쳐

- API Gateway : 외부 API 요청을 내부로 연계(routing), 로드밸런싱, 필터링, 인증/인가, API 관리 기능 제공
  - Spring Cloud Gateway
- Service Mesh(그물망) : 내부 서비스간 통신/호출 관리, API Mediation(API 변환등을 통한 프로토콜 중재)를 위해 필요한 기술
  - Service discovery, Service Router, Circuit Breaker. API Gateway와 합칠수도 있음.
    - Service discovery(Eureka) : 분산 환경에서 동적으로 생성/변경/삭제되는 서비스 인스턴스 정보를 자동으로 등록/관리
    - Service Router : Client 요청을 적절한 서비스 인스턴스로 Forwarding. 로드밸런싱이 핵심 기능.
  - 동적 디스커버리, 라우팅, 로드밸런싱 등 확장 서비스 지원이 가능
  - 셀프 힐링이나 Circuit breaker 같은 안정성 패턴 지원
- Container Management : 서비스 실행을 위한 Container 환경 제공
  - k8s, Docker 등
- Backing Service : 데이터를 처리, 서비스간 데이터 저장, 비동기 통신, 이벤트 전달
  - Data Backing Service + Message Backing Service
  - Message queue, MOM(메시지 기반 미들웨어)
- Telemetry : 원격(Tele)+측정(Metry). 로그 확인 및 추적 등의 추적/분석 도구
- CI/CD : 소스 Commit 부터 배포까지 자동화된 절차를 지원

- 환경
  - Spring Boot : 다양한 디펜던시를 빠르게 적용하고 스프링을 단독 실행 가능하게 함. 자바 백엔드서버 개발 환경에서 필수.
    - 내장서버, 다양한 Starter Component, 환경 자동 설정, 설정파일로 XML 대신 properties나 yaml 활용환경 제공.

## Spring Cloud

- 개요 : 분산 시스템 상에서 필요한 내용을 쉽게 구축할 수 있게 하기 위해 Netflix에서 제공한 오픈소스 dependency(OSS)
- Hystrix : Circuit-breaker. 특정 MS의 장해가 다른 MS의 장해를 일으키는 것을 방지
  - 기능
    - Timeout, 장애 대응에 미리 정해둔 루트를 따라 처리하게 설정할 수 있음
    - 임계치를 넘는 요청에 우회 설정을 해둘 수 있음
  - 적용
    1. dependency 적용
    2. Main app에 @EnableCircuitBreaker 추가
    3. Circuit break 추가하려는 로직에 @HystrixCommand 추가
- Eureka : Server Discovery. 서비스들의 목록과 위치가 동적으로 변하는 환경하에서 서비스를 효율적으로 관리
  - Eureka Server : Eureka Service를 자기 등록하고 Client가 가용한 서비스 목록을 요청하는 서버
    - Main에 @EnableEurekaServer 붙은 쪽
  - Eureka Client : 서비스의 위치 정보를 Eureka Server로 부터 Fetch 하는 서비스
    - Main에 @EnableEurekaClient 붙은 쪽
- Spring Gateway : API Gateway. 각 서비스들의 IP와 PORT에 관한 단일화된 엔드포인트 제공
  - 각 서비스에 필요한 인증/인가, 사용량 제어, 요청 응답 변조등의 기능 담당
  - 라우팅 + 로드밸런싱 + Mesh 연계 + Filtering + Logging/Monitoring
  - Main에 @EnableEurekaClient 필요.
  - 라우팅 설정 등록 예시

    ```YAML
    spring:
    application:
      name: apigateway-service
    cloud:
      gateway:
        routes:
          - id: spring-service
            uri: lb://SPRING-SERVICE
            predicates:
              - Path=/spring-service/**
          - id: flask-service
            uri: lb://FLASK-SERVICE
            predicates:
              - Path=/flask-service/**
          - id: go-service
            uri: lb://GO-SERVICE
            predicates:
              - Path=/go-service/**
    ```

- 흐름
  1. 요청이 Spring Gateway로
  2. Spring Gateway는 처리할 수 있는 인스턴스를 Eureka Server(서비스 디스커버리)에서 검색
  3. 찾은 인스턴스에 Gateway가 처리를 요청 (+로드밸런스 활용)
  4. Gateway가 응답을 받고 해당 내용을 Client에게 응답
