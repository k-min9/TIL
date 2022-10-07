# API Gateway Service

사용자나 외부 시스템의 요청을 처리하게 하는 proxy 역할

시스템 내부 구조는 숨기고, 외부 요청에 대한 적절한 응답을 해줄 수 있음

- 역할 및 주요 기능
  - 인증 및 권한 부여
  - 서비스 검색 통합
  - 응답 캐싱
  - 정책, 회로 차단기 및 QoS 다시 시도
  - 속도 제한
  - 부하 분산
  - 로깅, 추적, 상관관계
  - 헤더, 쿼리 문자열 및 청구 변환
  - IP 허용 목록에 추가

- Netflix Ribbon
  - Spring Clud에서의 MSA간 통신 : RestTemplate, Feign Client
  - 비동기화 처리가 잘 안되어서 최근에는 사용하지 않음
    - 심지어 maintenance 상태(새로운 기능을 추가하지 않겠다.)
- Netflix Zuul
  - Gate역할을 해주는 제품
    - 마찬가지로 maintenace 상태
- Spring Cloud Gateway
  - Tomcat이 아닌 Netty 서버 사용
  - 비동기 방식을 지원!

## 구현

- Dependency : Devtools, Eureka Discovery Client, Gateway

1. application.yml 작성

```yaml
server:
  port: 8000

# 유레카와 연동할 예정
eureka:
  client:
    register-with-eureka: false
    fetch-registry: false
    service-url:
      defaultZone: http://localhost:8761/eureka

spring:
  application:
    name: gateway-service
  # gateway 핵심 정보
cloud:
    gateway:
      routes:
        - id: first-service  # 고유 ID
          uri: http://localhost:8081/  # 포워딩 위치
          predicates:
            - Path=/first-service/**  # 조건 (이 주소로 올 경우 8081로 보내겠다는 소리)
          filters:
            - AddRequestHeader=first-request, first-requests-header2
            - AddResponseHeader=first-response, first-response-header2
        - id: second-service
          uri: http://localhost:8082/
          predicates:
            - Path=/second-service/**
          filters:
            - AddRequestHeader=second-request, second-requests-header2
            - AddResponseHeader=second-response, second-response-header2
```

- 결론 : 이 상태로 이동시 </first-service/**> 는 </localhost:8081/first-service/**>로 이동하게 됨.
service가 포함된 주소가 어색하면 다른 방법으로 최적화 필요

## Filter

Gateway Handler Mapping : 들어온 정보 확인

Predicate :  사전 조건
Pre filter : 사전 필터,
Post filter : 사후 필터,

필터는 application.yml 설정과 java 코드 두 종류가 있음.
yml 타입은 위의 application.yml이 예제고,
아래가 java code 필터를 이용하여 Client 요청을 가로채서 추가적인 header 넣기 예제

```java
// <FilterConfig.java>
@Configuration
public class FilterConfig {

    @Bean
    public RouteLocator gatewayRoutes(RouteLocatorBuilder builder) {
        return builder.routes()
                .route(r -> r.path("/first-service/**")
                        // request나 response에 헤더를 붙여서 받거나 내보낼 수 있음
                        .filters(f -> f.addRequestHeader("first-request", "first-request-header")
                                       .addResponseHeader("first-response", "first-response-header"))
                        .uri("http://localhost:8081"))
                .route(r -> r.path("/second-service/**")
                        .filters(f -> f.addRequestHeader("second-request", "second-request-header")
                                .addResponseHeader("second-response", "second-response-header"))
                        .uri("http://localhost:8082"))
                .build();
    }
}
```

AuthenticationFilter, AuthorizationHeaderFilter : Gateway에서 제공하는 인증/인가 Filtering 기능

### 고도화

Custom Filter, Global Filter(cloud.gateway.default-filters), Logging도 만들고 등록할 수 있다.

```yaml
# Filter에 추가정보 보내기

filters:
  - name: LoggingFilter
    ars:
      baseMessage: Hi  # 해당 변수에 input 됨
      preLogger: true
      postLogger: true
```

OrderedGateWay를 사용하면 Filter의 순서를 조절할 수 있다.

## Eureka와 연동

Flow : 요청 → Gateway → Eureka → Gateway → Service → Gateway → 반환

1. Gateway에 Eureka-client 추가 후 yml에 관련 설정 true 및 defaultZone 등록
그 후, Gateway routes의 uri를 [http://localhost:8081](http://localhost:8081) → lb://MY-FIRST-SERVICE 등으로 변경
2. 관련 서비스도 마찬가지로 Eureka-client에 등록
3. Gateway 서비스 이용
