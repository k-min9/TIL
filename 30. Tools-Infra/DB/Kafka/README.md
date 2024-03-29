# Apache Kafka Application Programing

- 개요 : 인프런 강의

## 아파치 카프카의 역사와 미래

- 탄생배경 : 링크드인에서 파편화된 데이터 수집 및 분배 아키텍쳐 운영에 어려움이 있었음
  - 아키텍쳐가 거대해지고, 소스 app과 타겟 app의 갯수가 늘어나면서 전송라인이 기하급수적으로 복잡해짐
  - 카프카는 각각의 App을 연결하여 data를 처리하는것이 아니라 한 곳에 모아(Unified Log) 처리할 수 있도록 중앙집중화 함
- 구조 : 케시지 큐와 동일한 FIFO 구조
  - 파편화된 데이터파이프라인의 복잡도를 낮출수 있음
  - 소스 애플리케이션과 타깃 애플리케이션 간의 커플링을 제거
  - 한쪽의 이슈가 다른 app에 영향을 미치는 의존도를 타파
    - 데이터를 어느 app에 넣을지 고민하는 것이 아니라 카프카로 넣으면 된다
  - 프로듀서(데이터를 큐에 보냄)과 컨슈머(데이터를 큐에서 가져감)로 구선
- 특징
  - 높은 처리량
    - 많은 양의 데이터를 묶음단위로 처리하는 배치로 빠르게 처리하고 네트워크 통신을 최소한으로 함
    - 파티션 단위를 통해 동일 목적 데이터를 여러 파티션에 분배하고 데이터를 병렬 처리
      - 파티션 개수 만큼 컨슈머 개수를 늘려 동일 시간당 데이터 처리량 증가
  - 확장성
    - 카프카 클러스터의 브로커를 통해 자연스러운 스케일 아웃과 스케일 인을 지원 (무중단)
  - 영속성 : 프로그램을 종료해도 데이터가 사라지지 않음
    - 카프카는 다른 메시징 플랫폼과 다르게 전송 데이터를 메모리가 아닌 파일 시스템에 저장
      - 파일 시스템이면 느려보이지만 운영체제 레벨에서 페이지 캐시(Cache) 영역을 만들고 재접근을 빠르게 하는 방식등을 활용하여 속도를 보장
    - 파일 시스템 덕에 브로커 애플리케이션이 장애가 발생해 종료되도 프로세스 재시작으로 안전한 처리가 가능
  - 고가용성
    - 카프카 클러스터는 3개 이상의 서버로 운영
    - 복제 옵션 : 프로듀서로 받은 데이터를 여러 브로커 중 1대만이 아닌 여러 브로커에 저장
      - 옵션에 따라 리전 단위의 장애에도 데이터를 안전하게 복제할 수 있음
- 역사
  - 초기 : 엔드 투 엔드로 데이터를 배치로 모음
    - 원천 데이터로부터 파생된 데이터의 히스토리 파악하기 힘듬
    - 계속된 데이터 가공으로 인한 데이터 파편화 > 데이터 거버넌스(데이터 표준 및 정책) 준수가 난해
  - 람다 아키텍쳐 : 3가지 레이어로 구성 (구조 : 원천 > 배치-느림,일괄, 스피드-빠름 > 서빙)
    - 배치 레이어 : 배치 데이터를 모아 특정 시간, 타이밍마다 일괄 처리
    - 서빙 레이어 : 가공된 데이터를 데이터 사용자와 서비스 app이 사용할 수 있도록 저장
    - 스피드 레이어 : 서비스로부터 생성된 원천 데이터를 실시간으로 분석
      - 카프카가 여기에 위치
    - 단점 : 로직 파편화, 디버깅, 배포, 운영 분리 이슈 발생
      - 원천 데이터를 처리하는 곳이 두 개이기 때문에, 로직이 2배로 필요하거나 융합할때 다소 유연하지 못함
        - 1개의 로직을 추상화하고 각각의 레이어에 적용하는 서밍버드가 있었지만 완전해결은 아니었음
  - 카파 아키텍쳐 : 람다 아키텍쳐에서 배치레이어를 제거하고 스피드 레이어에서 모든 데이터를 처리
    - 활용 : 배치데이터 표현시, 시간, 일자 등 전체 데이터가 백업된 스냅샷 데이터가 아닌 시간 순서대로 기록한 변환 기록 로그(change log)를 활용함으로서 스냅샷 데이터 저장 없이 배치데이터 표현이 가능
    - 구분
      - 배치 데이터(ex-하둡)
        - 한정적 데이터 처리
        - 대규모 배치 데이터를 위한 분산처리 수행
        - 분, 시간, 일 단위 처리를 위한 지연 발생
        - 복잡한 키 조인 수행
      - 스트림 데이터
        - 무한 데이터 처리
        - 지속적으로 들어오는 데이터를 위한 분산 처리 수행
        - 분 단위 이하 지연 발생
        - 단순한 키 조인 수행
        - 로그에 시간을 남기는 것으로 스트림 적재 데이터도 배치로 처리할 수 있음
  - 스트리밍 데이터 레이크 : 카파 아키텍쳐에서 서빙 레이어를 제거. 스피드 레이어만 남음
    - 스피드 레이어에 대규모 데이터를 저장(롱 텀 저장소)하고 사용할 수 있게 해서 이중으로 관리되는 운영 리소스를 감소
    - 자주 접근하는 데이터와 그렇지 않은 데이터를 구분해서 후자를 오브젝트 스토리지 같은 저렴한 저장소에 저장하고 자주 쓰는 데이터만 브로커에서 사용하는 작업이 필요

## 카프카 기본 개념

- 카프카 브로커 :카프카 클라이언트와 데이터를 주고받기 위해 사용하는 주체 (애플리케이션 서버)
  - 데이터를 분산저장하여 발생하는 장애를 막고 안전하게 사용할 수 있게 함
  - 1 서버 당 1 카프카 브로커
  - 3대 이상의 브로커 서버를 1개의 클러스터로 묶어서 운영
    - 묶인 브로커간 분산 저장 및 복제를 수행
  - 컨트롤러 : 다수 브로커 중 선정 된 한대의 브로커
    - 브로커들의 상태 체크와 필요하면 파티션을 재분배
    - 문제가 생긴 브로커와 컨트롤러의 빠른 교체가 가능
  - 복제 : 카프카의 가장 중요한 시스템 중 하나
    - 카프카가 장애 허용 시스템(Fault talerant System)으로 동작하게 되는 원동력
    - 일부에 장애가 발생해도 데이터 유실없이 안전히 사용
    - 복제는 리더와 팔로워로 구성되어 리더는 직접 통신하고, 팔로워가 복제데이터를 가짐
    - 문제가 발생할 경우 팔로워가 리더가 되어 안정적인 서비스를 운영
    - ISR : 리더와 파티션이 완전히 싱크(오프셋 수가 같음)됨
- 주키퍼 : 카프카 클러스터 실행을 위해 필요
- 컨슈머 : 특정 파티션으로부터 데이터를 가져가고 어디까지 가져갔나 오프셋을 커밋
  - 데이터를 가져갈때 토픽 데이터가 삭제되지도 않고, 삭제 요청할수도 없음
- 세그먼트에 데이터를 저장. 삭제단위가 됨.
  - 마지막 세그먼트는 액티브 세그먼트가 되어  삭제 대상이 되지 않음
- 토픽 : 데이터 구분 단위. 1개 이상의 파티션을 소유
  - 여러 개의 파티션 소유시 0번 브로커부터 round-robin하게 파티션 생성
    - 그 외에도 통신 집중을 막고 선형 확장을 하기 위한 파티션 분산 스킬이 있음
  - 파티션에는 프로듀서가 보낸 데이터(레코드)들이 저장.
  - 파티션을 통해 컨슈머들이 레코드를 병렬로 처리하게 매핑
    - 컨슈머를 늘리면서 파티션 갯수를 늘리면 처리량이 증가

## 프로듀서와 컨슈머

- 프로듀서 : 데이터의 시작점. 필요한 데이터를 선언하고 브로커의 특정 토픽 파티션에 전송
  - 전송 후, 파티셔너, 배치생성 단계를 지님
  - 멱등성 프로듀서(idempotence)
    - 멱등성 : 여러번 연산을 수행하더라도 동일한 결과가 나옴
    - 네트워크 이슈와 상관없이 정확히 한번 전달하고 싶을때 사용
      - 기본 동작 방식(At least once)에서 정확히 한번 전달(exactly once)로 변환
      - 프로듀서 고유 ID(PID)와 레코드 전달번호(SID)를 보내서 구현
        - 세션이 끊어지는 사태 발생시, PID가 달라져서 무력화 됨
        - PID, SID 저장을 위한 공간이 필요하니 일종의 트레이드 오프
      - 제대로 된 ACK가 돌아올때까지 retry하는것이 기본 골자
    - 데이터의 중복 적재를 막음
  - 트랜잭션 프로듀서 : 레코드를 트랜잭션 단위로 묶을지 여부 설정. atomic 성질을 부여
    - 프로듀서별 고유 트랜잭션 ID가 필요
    - 프로듀서/컨슈머별 isolation level을 설정할 수 있음
- 컨슈머 : 브로커로부터 데이터를 가져와 필요한 처리를 함
  - 커밋 : 브로커로부터 어디까지 데이터를 가져갔는지 기록한다.
  - 멀티 스레드 컨슈머 : 파티션과 컨슈머를 동일하게 맞추고 병렬 연산하는 것을(1개의 스레드를 가진 n개의 프로세스 운영) n개의 스레드를 가진 1개의 프로세스로 운영
  - 컨슈머 랙 : 최신 오프셋과 컨슈머 오프셋 간의 차이
    - 컨슈머 그룹, 토픽, 파티션 별로 생성될 수 있으며 이를 모니터링해서 컨슈머와 파티션 숫자를 늘려 병렬 연산 속도를 늘린다 등의 대응을 할 수 있다.
      - 모니터링 하여 임계치를 넘으면 알려주는 외부 툴() 등을 활용하면 좋음

## 카프카 커넥트

- 개요 : 데이터 파이프라인 생성시 반복 작업을 줄이고 효율적인 전송을 돕는 애플리케이션
  - 작업 형태를 템플릿(커넥터) 형태로 만들어 실행
- 커넥터 : 커넥트가 커넥터를 만들고 안에서 다수의 태스크를 실행
  - 애플리케이션은 커넥터를 통해 카프카로 데이터를 보내오고 받아올 수 있음
  - 단일모드(Stand alone, 단일 프로세스)와 분산모드(Distribution, 멀티 프로세스)가 존재함.
  - 70개가 넘는 옵션과 100개가 넘는 Plugin 제공
- 종류
  - 소스 커넥터 : 프로듀서
  - 싱크 커넥터 : 컨슈머
