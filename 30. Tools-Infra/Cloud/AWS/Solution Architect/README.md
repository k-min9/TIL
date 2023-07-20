# SAA

- AWS Certified Solutions Architect Associate
  - SAA-C03
  - 65개 문항 130분 150달러
  - 1000점 중 720점 이상
- 시험 진행
  - 온라인/오프라인
  - 한글로 언어 신청 : 한글/영문 동시 제공됨
- aws.training
  - 자격증 계정 만들고 시험 등록
  - 시험 합격시 혜택에 50% 할인 쿠폰

## 개요

[시험 정보와 안내서](https://aws.amazon.com/ko/certification/)

- 도메인
  - 보안
  - 복원력
  - 고성능
  - 비용

## 보안 아키텍쳐 설계

- 키워드 : 인증과 접근제어
  - 리소스에 대한 보안 액세스 설계
  - 안전한 워크로드 및 애플리케이션 설꼐
  - 적절한 데이터 보안 제어 결정
- 서비스
  - IAM : 사용자 인증 서비스
  - Organizations : 조직. 수많은 계정의 통제가 가능해짐
  - VPC : Virtual Private Cloud
  - Cloud Front : 캐싱해둔 데이터를 둘 수 있게 하여 S3등에 대한 접근을 줄임
  - WAF : 방화벽. Cross-Site, DDOS 같은 간단한 공격을 탐지하고 막아줌
  - VPN : 회사와 VPC 간의 연결을 위한 채널을 만들어 줌
  - PrivateLink : 예를 들어 VPC와 S3 등을 다이렉트로 연결하는 사설링크
    - ENI카드를 VPC에 만들어 사설 IP로 통신
- 보안 설계 전략
  - 추적성
  - 여러 AWS 계정
  - 보안 표준 적용
  - 자동화
  - Macie : 주민번호등 문제가 생길수있는 정보를 식별하고 별도 보관
  - Cognito : 인증
- 규정 요구사항 : 멀티 테넌스(하나의 보안 자료를 여럿이서 씀) 하지 말라면 KMS(Key Management Service)에서 HSM으로 변경
- 백업 전략 : 주기적, 지속적 > AWS Backup
  - EBS 스냅샷, 다이나모DB백업, RDS 스냅샷, Aurora 스냅샷...
    - RDS와 Aurora는 기본 스냅샷으로 S3에 저장됨. 매뉴얼 Plan, 자동 Plan(5분 실시간) 제공

## 복원력이 뛰어난 아키텍쳐 설계

- 개요
  - 장애 발생시 해결하거나 중단 최소화
- 도메인
  - 확장 가능하고 느슨하게 결합된 아키텍쳐
    - 컴퓨팅 워크로드
      - EC2
      - EKS, ECS : 컨테이너 서비스 > 자동 확장
      - ElasticCache : key-value. 인메모리
      - RDS proxyInstance
    - Decoupling 기법
      - 로드밸런서 : Elastice Load Balancing
      - Amazon SQS(Simple Queue Service) : WEB과 APP 사이에 메시지 큐를 저장할 곳을 만들어둬서 App이 한가해지면 가져가서 작업함
      - Amazon EventBridge, Amazon DynamoDB의 변경이력(Stream) 활용
  - 가용성이 높고 내결함성이 뛰어난 아키텍쳐
    - 고가용성(HA) : 다운타임 최소화
    - 내결함성(FT) : 다운타임이 없게
    - 재해복구 : 리전등이나 가용영역 이슈
      - BackUp&Restore, Pilot Light, Warm Standby, Multi-site active : 우측
    - 복구시점목표(RPO) : 내가 원하는 백업시점
    - 복구시간목표(RTO) : 서비스 중단에서 복원까지 최대 허용되는 지연시간
    - Auto Scaling을 통한 복구

## 고성능 아키텍쳐 설계

- 도메인
  - 파일 ; 오브젝트 : S3, 블록 : EBS, 파일 : EFS
  - DB ; 관계형 : RDS < Aurora(데이터 공유 방식으로 인해 RDS보다 빠름), OLAP : RedShift, DynamoDB : DAX 캐싱 지원
  - 네트워킹 ; VPC, Private Link(내부연결), Route53(DNS) 중 resolve 서비스를 통한 IP 접속, Global Accelerator : 리전간 로드밸런스 역할
  - 데이터 수집 및 변환
    - 아테나

## 비용 최적화 아키텍쳐 설계

- 비용 절약
  - AWS Budget : 예산 강제화
- 도메인
  - 스토리지
    - 컴퓨팅
    - DB
    - 네트워크
