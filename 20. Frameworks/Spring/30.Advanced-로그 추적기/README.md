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
