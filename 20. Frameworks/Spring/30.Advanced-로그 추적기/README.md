# 로그 추적기

- 배경
  - 애플리케이션이 커지면서 점점 모니터링과 운영이 중요해지는 단계.
  - 어떤 부분에서 병목이 발생하는지, 예외가 발생하는지를 로그를 통해 확인하는 것이 점점 중요해지고 있다
- 요구사항
  - 모든 public 메서드의 호출과 응답 정보를 로그로 출력
  - app의 흐름을 변경하거나, 비지니스 로직 동작에 영향을 주면 안됨
  - 메서드 호출에 걸린 시간
  - 정상 흐름과 예외 흐름 구분 (예외 발생시 정보가 남아야 함)
  - 메서드 호출 깊이 표현
  - ID를 통한 HTTP 요청과 트랜잭션 구분

  ```Java
    [796bccd9] OrderController.request()
    [796bccd9] |-->OrderService.orderItem()
    [796bccd9] | |-->OrderRepository.save()
    [796bccd9] | |<--OrderRepository.save() time=1004ms
    [796bccd9] |<--OrderService.orderItem() time=1014ms
    [796bccd9] OrderController.request() time=1016ms
    예외 발생
    [b7119f27] OrderController.request()
    [b7119f27] |-->OrderService.orderItem()
    [b7119f27] | |-->OrderRepository.save()
    [b7119f27] | |<X-OrderRepository.save() time=0ms
    ex=java.lang.IllegalStateException: 예외 발생!
    [b7119f27] |<X-OrderService.orderItem() time=10ms
    ex=java.lang.IllegalStateException: 예외 발생!
    [b7119f27] OrderController.request() time=11ms
    ex=java.lang.IllegalStateException: 예외 발생!
  ```

P.S. 요구사항 자체는 모니터링 툴 도입하면 애초에 해결이 되긴 함. 기술 습득이 목적.

## 최초 구현

- 모든 요구사항을 만족한 서버를 구성하였다.
- 문제점
  - 깊이 표현을 위한 traceId 동기화 필요
    - 관련 메서드, 클래스, 인터페이스를 모두 수정하였음
    - 호출 메서드가 초기호출(begin)과 내부호출(beginSync)로 구분되어 깊이 변경, 상호간 호출이 불편해짐

## Thread Local

- 제기 : traceId를 파라미터로 넘겼더니 모든 메서드에 이를 추가해줘야 했음
  - 더 좋은 방법은 없을까
- 결론 : FieldLogTrace 구현체에 traceIdHolder 필드를 만들어 깔끔하게 저장하자.
- 문제 : FieldLogTrace는 Bean에 등록된 싱글톤이므로 동시성 문제 발생
- 해결 : ThreadLocal / 쓰레드 별로 별도의 데이터 저장소를 가지게 하자

  ```Java
    private ThreadLocal<String> nameStore = new ThreadLocal<>();

    ...(로직)


    nameStore.remove() // 필수!!!! 
    // 같은 쓰레드를 사용하게 되는 타 사용자가 전에 남아있던 데이터를 볼 수 있음
  ```
