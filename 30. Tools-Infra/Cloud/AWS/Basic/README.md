# AWS

- 개요 : 아마존에서 On-Promise를 클라우드 서비스로 만든 것
- 알기 쉬운 On-promise와 Cloud간 용어 매칭
  - 방화벽, ACL, 관리자권한, 네트워크, 서버, NAS, 디스크, DB
  - 보안그룹, NACL, IAM, VPC, EC2, EFS, EBS, RDS
    - 여기서 E로 시작하는 것은 죄다 Elastic(탄력적)임을 표방
- 흐름
  1. Route53이 도메인에 대한 응답을 한다.  (DNS포트가 53이라 Route53)
  2. 서버 EC2로 접속 한다.
  3. 로컬 디스크인 EBS(Elastic Block Store)에서 데이터를 읽는다.
  4. 요청한 데이터가 있으면 RDS, DynamoDB(NoSQL)에서 읽어오거나, S3 스토리지에서 이미지나 첨부파일을 다운받아 사용
- 구성 : 리전 > 가용 영역(AZ) > 데이터센터 > 엣지네트워크
  - 리전 (Region) : 데이터 센터를 클러스터링 하는 물리적 위치.
    - 2개 이상의 가용 영역으로 구성
    - 재해복구 설계 : 2개 이상의 리전에 시스템을 배치하여 다른 리전에 재해가 발생해도 복구할 수 있게 설계
  - 가용 영역 (Availability Zone – AZ)
    - 1개 이상의 개별 데이터 센터로 구성
    - 각각 물리적으로 떨어져 있고, 고속 네트워크로 연결됨
    - 고가용성 설계 : 다중 AZ(Multi AZ), 2개 이상의 가용 역역에 시스템 배치
  - 엣지 로케이션(Edge Location) : 콘텐츠를 캐싱하여 사용자에게 더 짧은 지연 시간으로 콘텐츠를 전송
    - 글로벌 배포서비스인 AWS CloudFront, Global Accelerator에서 대표적으로 사용
    - ex) 서울에서 미국 리전의 데이터에 접속할때 서울 엣지 로케이션에 미리 캐싱
- 엣지 인프라 서비스
  - AWS Outposts : 클라우드를 온프라미스에서도 쓸수 있도록 확장한것
  - AWS Local Zones : 대형 메트로 센터 사용, 엣지 서비스
  - AWS Wavelength : 5G 네트워크 엣지 서비스

## 컴퓨팅 서비스

- EC2(Elastic Compute Cloud) : 서버
  - 인스턴스 패밀리
    - 범용
    - 컴퓨팅 최적화 : 고성능 웹서버. 동영상 인코딩
    - 메모리 최적화 : 고성능 DB. 분산 메모리 캐쉬
    - 스토리지 최적화 : 데이터 웨어하우징
    - 액셀러레이티드 컴퓨팅 : 3D 시각화, 기계 학습
  - 요금
    - 온디맨드
    - 예약 인스턴스(RI) : 장기 계약(1년, 3년...)시 할인. 특정 가용 영역에 지정 가능.
    - Savins Plan : 상대적으로 할인율이 낮음
    - Spot 인스턴스 : 미사용 서버를 임시로 사용하여 최대 90% 저렴. 언제든지 종료될 수 있음.
- 컨테이너 관리 서비스
  - ECS : 컨테이너가 소수일때 채용. 많아질때는 관리형 사용이 필요하며 확장이 용이
  - EKS(Elastic K8s Service) : 컨테이너 관리로 쿠버네티스를 활용한 AWS 쿠버네티스 관리 오케스트레이션 서비스
- AWS lambda : 서버리스 컴퓨팅
  - 장점 : 서버 관리에 들어갈 리소스를 개발에만 집중할 수 있음. 트래픽 당 가격이기 때문에 일반적으로 24시간 구동이 되는 EC2 보다 저렴

## 스토리지, DB

- 스토리지 옵션
  - S3  : 일반/오브젝트(객체) 스토리지. 파일 스토리지 아님. 높은 내구성. 이미지/비디오에 적합. EBS보다도 저렴
    - 단위 : 버킷, 접근 방식이 계층적이 아니라 객체적
    - 사용자 제어 및 액세스 로그 관리가 가능
    - 데이터레이크(대량의 데이터를 저장, 처리, 보호하기 위한 중앙 집중식 저장소. 머신러닝, 분석, 보안 특화)로 사용하기 적당
  - S3 Glacier : 장기 보관용 S3
  - EFS(Elastic File System) : EC2용 관리형 파일 스토리지. 높은 가용성+보안. On-Promise의 NFS, NAS와 유사/동일한 서비스.
    - NAS : 파일 서버. 파일 레벨로 액세스. 비구조적 데이터에 사용.
  - EBS(Elastic Block System) : 하드 디스크. EC2에서 사용하는 디스크 저장소로 클라우드에서 SAN을 구축. EFS의 10% 정도의 가격
    - SAN : 하드 디스크. 블록 레벨 데이터 저장 구조적 데이터에 사용.
  - Storage Gateway : 클라우드 스토리지에 대한 On-promise의 액세스 권한 제공.
- 데이터 베이스 : 기본적으로 완전 관리형(설정 인스턴스 등의 지정이 필요 없음)
  - RDS : 관계형 DB. MySQL, Postgre등과 완전 호환, 아마존 오로라 제공
  - DynamoDB : NoSQL. 자동 파티셔닝으로 짧은 지연시간을 보장.
    - 파티셔닝 : DB를 분할하여 조회 성능을 올리고 관리를 쉽게 함.
  - DocumentDB : 문서형 데이터 처리. MongoDB와 호환.
    - MongoDB : JSON 형태의 동적 스키마형 문서(BSON)를 사용하는 NoSQL. Document, Collection이 각각 RDBMS의 row와 column의 대응
      - ACID, 특히 일관성을 포기한 대신 같은 조건하에서 RDBMS보다 빠르다!
  - ElasticCache : REDIS와 MEMCACHED를 사용하는 인메모리 캐쉬 서비스. 읽기와 고속 분석 특화
    - Memcached : 유명한 분산 메모리 캐시 시스템
    - Redis : String, Hash, List, Set, Sorted Set 등 다양한 데이터 형식을 제공하는 키-값(Key-Value) 데이터 저장소
  - RedShift : AWS 데이터 웨어하우스
  - Neptune : AWS graphDB
    - graphDB : 그래프의 형태로 데이터를 표시하고 DB를 저장
  - QLDB(Quantum Ledger) : 원장 DB. 굳이 블록체인을 쓰지 않더라도 원장을 구현하여 투명하고 변경 불가능한 트랜잭션 로그를 제공.

## 네트워크

- 개요 : VPC. Virtual Private Cloud가 네트워크에 대응
- 보안 : VPC > NACL(서브넷 단위) > 보안 그룹(EC2 단위) > 있다면 추가적인 서브파티
- ELB : NLB(L4), ALB(L7), GWLB, CLB(Deprecated)
  - 자세한건 [70. Computer Science\5.네트워크\01 AWS Certified Advanced Networking]에 정리
- Route53 : 네임서버
- 책임
  - AWS 책임 : 기초 서비스, 글로벌 인프라
  - 고객 책임 : 고객 데이터 관리
- IAM(Identity and Access Management) : 사용자, 그룹, 역할에 권한을 할당하고 인증 및 권한 부여.
  - 정책
    - 자격증명 기반 : AM 사용자 , 그룹, 역할
    - 리소스 기반 : S3 버킷 등의 리소스에 액세스할 수 있는 대상 및 해당 대상이 리소스에서 수행할 수 있는 작업을 지정

## 기타

- CloudTrail : 사용자 활동과 API 사용 추적
- Trust Adviser : 비용 최적화, 성능, 보안, 내결함성, 서비스 한도 관련 서비스 제공
