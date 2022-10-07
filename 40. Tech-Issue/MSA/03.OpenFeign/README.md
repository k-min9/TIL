# OpenFeign

Service Discovery, Service Registry 서비스

- 개요 : MS간 통신
- Openfeign vs restTemplate
  - restTemplate : 전통적인 spring api 호출 구조.(22.10. 기준 Webclient로 전환 중)
  - openfeign : REST call을 추상화한 interface를 작성하고 annotation을 선언 하기만 하면 되는 방식.
    - 불필요한 중복 코드 작성을 없애고, 직관적으로 포함되어있는 애플리케이션 쓰듯이 쓸 수 있음
    - 가독성이 좋아지며 설정이 간편해져 비지니스 로직에 집중할 수 있음
- 설정
  1. spring cloud starter-openfeign dependency 추가.
  2. main에 @EnableFeignClients 추가. 이후 @FeignClient 선언 만으로 구현체를 만들어 줌.
  3. 인터페이스 선언후, @FeignClient(name="요청 MS이름", url="유레카 설정시 생략가능", fallback)등 필요한 설정
      - 번외) Hystrix 설정시, 실패에 대한 callback 함수 설정 가능
  4. 이후 필요한 service에서 생성자 주입받아 포함 앱 마냥 사용
- 예외 처리
  - 간단한 try ~ catch 활용
  - ErrorDecoder 제공있음
