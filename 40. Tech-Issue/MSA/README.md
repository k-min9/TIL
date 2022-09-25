# MSA (Micro Service Architecture)

- 개요 : 여러 작은 서비스들로 구성된, 서비스의 집합인 Application을 개발
- 배경 : 모놀릭 통합 빌드/배포로 추가/변경 요구사항 대응이 점점 어려워짐
- 모놀릭(Monolithic)과의 차이점
  - 장점
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
      - 이 외에도 분산 데이터 조회, 모니터링, 호출 추적이 어렵지만 별도 방안으로 해결 가능(Cost 증가)
- 용어
  - IPC : Inter-Process Communication, 프로세스간 통신.
