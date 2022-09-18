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

## 예외

- 일반적인 예외 상황 상정
  - 체크 예외 : 비지니스 예외
    - ex) 시스템은 제대로 동작했지만, 잔고가 없었다.
    - 커밋하자!
  - 언체크 예외 : 복구 불가능 예외 (=런타임 예외, 시스템 장애)
    - 롤백하자!

## 전파 (PROPAGATION)

- 개요 : 트랜잭션이 이미 진행중인데, 여기에 추가로 트랜잭션을 수행하면 어떻게 될까?
- 배경 : 기본 옵션 REQUIRED 기준 설명
설정을 REQUIRES_NEW로 설정할 경우, 외부 내부가 각각의 DB 커넥션을 가지고 서로 커밋에 영향을 주지 않음
- 결론 : 두 개의 트랜잭션을 합쳐서 하나의 트랜잭션으로 만들어준다.
  - 옵션(isolation , timeout , readOnly 등)은 트랜잭션이 처음 시작될 때만 적용
- 트랜잭션 종류
  - 논리 트랜잭션 : 묶이는 단일 트랜잭션, 처음 트랜잭션이 물리 트랜잭션 전체를 관리
  - 물리 트랜잭션 : 묶은 총 트랜잭션, 모든 논리 트랜잭션 커밋시 커밋, 하나라도 실패시 롤백
- 종류
  - REQUIRED : 기본, 주로 이 방식
  - REQUIRES_NEW : 무조건 새로 만듬
  - SUPPORT : 없으면 없는대로, 있으면 참여
  - NOT_SUPPORT : 트랜잭션 없이 진행 (기존은 보류)
  - MANDATORY : 의무. 기존 트랜잭션 없으면 예외, 있으면 참여
  - NEVER : 기존 트랜잭션 없으면 그대로 진행, 있으면 예외
  - NESTED : 내부 트랜잭션이 외부에 영향을 안 줌 (내부 실패해도 외부 커밋)
    - 변경 예제

    ``` java
    DefaultTransactionAttribute definition = new DefaultTransactionAttribute();
    definition.setPropagationBehavior(TransactionDefinition.PROPAGATION_REQUIRES_NEW);
    TransactionStatus inner = txManager.getTransaction(definition);
    ```

- 요청 흐름
  - 요청 흐름 - 외부 트랜잭션 (처음 불린 로직 1 코드)
    1. txManager.getTransaction() 를 호출해서 외부 트랜잭션을 시작
    2. 트랜잭션 매니저는 데이터소스를 통해 커넥션을 생성
    3. 생성한 커넥션을 수동 커밋 모드(setAutoCommit(false))로 설정
        - 물리 트랜잭션 시작
    4. 트랜잭션 매니저는 트랜잭션 동기화 매니저에 커넥션을 보관
    5. 트랜잭션 매니저는 트랜잭션을 생성한 결과를 TransactionStatus에 담아서 반환, 여기에 신규 트랜잭션의 여부가 담겨 있다. isNewTransaction 를 통해 신규 트랜잭션 여부를 확인 가능. 현 시점에서는 true (신규 트랜잭션)
    6. 로직 1이 사용되고, 커넥션이 필요한 경우 트랜잭션 동기화 매니저를 통해 트랜잭션이 적용된 커넥션을 획득해서 사용
  - 요청 흐름 - 내부 트랜잭션 (외부에서 불린 로직2 코드)
    7. txManager.getTransaction() 를 호출해서 내부 트랜잭션을 시작
    8. 트랜잭션 매니저는 트랜잭션 동기화 매니저를 통해서 기존 트랜잭션이 존재하는지 확인
    9. 기존 트랜잭션이 존재하므로 기존 트랜잭션에 참여. (=아무것도 하지 않음)
        - 기존 트랜잭션인 외부 트랜잭션에서 시작한 물리 트랜잭션을 자연스럽게 사용.
          이후 로직은 자연스럽게 트랜잭션 동기화 매니저에 보관된 기존 커넥션을 사용
    10. 트랜잭션 매니저는 트랜잭션을 생성한 결과를 TransactionStatus 에 담아서 반환하는데, 마찬가지로 isNewTransaction 를 통해 신규 트랜잭션 여부를 확인할 수 있다. 기존 트랜잭션에 참여했기 때문에 당연히 false (신규 트랜잭션이 아님)
    11. 로직 2가 사용되고, 커넥션이 필요한 경우 트랜잭션 동기화 매니저를 통해 외부 트랜잭션이 보관한 커넥션을 획득해서 사용
  - 응답 흐름 - 내부 트랜잭션
    12.  로직2가 끝나고 트랜잭션 매니저를 통해 내부 트랜잭션을 커밋한다. (논리 커밋)
    13.  신규 트랜잭션이 아니기 때문에 실제 커밋을 호출하지 않는다.
  - 응답 흐름 - 외부 트랜잭션
    14. 로직1이 끝나고 트랜잭션 매니저를 통해 외부 트랜잭션을 커밋한다.
    15. 신규 트랜잭션이다. 따라서 DB 커넥션에 실제 커밋을 호출한다. (물리 커밋)
    16. 실제 데이터베이스에 커밋이 반영되고, 물리 트랜잭션도 끝난다.
