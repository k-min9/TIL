# 스프링 트랜잭션

스프링 트랜잭션을 더 깊이있게 학습하고, 또 스프링 트랜잭션이 제공하는 다양한 기능들을 자세히 알아보자.

## 트랜잭션

@Transactional 사용시 고려사항

- 옵션
  - value : 스프링 빈에 등록된 어떤 트랜잭션 매니저를 사용할 지 선정
    - ex) @Transactional("memberTxManager")
  - rollbackFor : 롤백 조건 설정
    - ex) @Transactional(rollbackFor = Exception.class) : 예외 발생시 롤백
  - timeout : 트랜잭션 수행시간 설정
  - readOnly : true로 변경시 읽기만 가능. 성능 최적화!
  - propagation : 전파 단계 설정
  - isolation : 격리 단계 설정
    - DEFAULT : 데이터베이스에서 설정한 격리 수준을 따른다.
    - READ_UNCOMMITTED : 커밋되지 않은 읽기
    - READ_COMMITTED : 커밋된 읽기 (일반적임)
    - REPEATABLE_READ : 반복 가능한 읽기
    - SERIALIZABLE : 직렬화 가능
