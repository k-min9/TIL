# CI/CD

- 개요 : App 빌드 및 배포와 인프라 Provisioning을 자동화하여 산출물을 짧은 주기로 고객에게 제공하는 방법
  - Continuous Integration : 지속적인 통합
  - Continuous Deployment : 지속적인 배포
- 장점
  - 자동화를 통해 코드에 집중할 수 있는 환경을 갖출 수 있음
  - 파이프라인 단계를 통해 배포 프로세스를 여러 단계로 나눠 유효성 검사를 주기적으로 다각도로 실행할 수 있음
- 배경 : 점점 커지는 App과 MSA 환경, 잦은 변경과 출시가 필요해져서 더 많은 Communication이 필요
  - Agile(프로세스 문화, 변화) + CICD(라이프사이클 도구) + DevOps(개발문화, 역할)
- Devops : SW 개발자와 IT 종사자들 사이 의사소통, 협업을 강조한 SW 개발 방법론
  - CALMS : 조직체계/문화, 프로세스와 기술
    - Culture : 학습과 협업 중시, Fail Early 빠르게 작게 실패해라
    - Automation : 자동화. 적은 Effort로 큰 효율
    - Lean : Big Batch -> Small Batch로
    - Measurement : 모든것을 모니터링. 시스템 가용성 중심 지표에서 사용자 접속자 수로
    - Share : 공통 목표 협업을 위한 원활한 의사소통.(CSR -> ChatOps;Slack 같은) 기능 중심이 아닌 서비스 중심의 Cell 조직
- 필요성
  - 빠른 주기로 문제를 빠르게 식별하고 해결하여 Snowball Effect를 막을 수 있음
  - 지속적인 배포를 통해 테스트 환경과 다른 운영환경에서의 문제를 확인할 수 있음

- 지속적인 통합
  - Webhook : Commit 되면 바로 Integration
  - 빌드 실패시 Slack, SMTP등을 통한 빠른 피드백
- 지속적인 배포
  - 배포환경으로 App 배포
  - 배포기법 : 롤링업데이트, 블루/그린, 카나리
- Infra as Code : 인프라를 코드로 관리함
  - 코드 수정 > 인프라 배포 > 테스트 > 계획수립
  - 형상관리가 가능해지고, 인프라 변경에 유연해지며 인프라 구성부터 App 배포까지 One Step 제공 가능
  - 재사용이 가능하여 DEV, PRODUCT 구별없이 쉽게 같은 환경을 구축할 수 있음

## 도구

- 배경 : 컨테이너의 등장으로 아키텍쳐 구조에 변화가 생겼고 클라우드 도입으로 다양한 환경을 갖출 수 있음

- Source Registry : 프로젝트 시작점이나 형상관리 관련
  - GitLab, BitBucket, Wire Code, AWS CodeCommit, Cloud Source Repo
  - 역사 : CVS -> SVN(중앙집중) -> Git(분산관리)
- CI : Build 쪽 치중 도구. 여럿이 개발한 코드를 통합
  - Jenkins : 많은 플러그인으로 확장성 우수
  - GitLab Runner
  - Wire Build : Atlassian에서 제공하는 상용 솔루션, Jira나 Bitbucket과 연동이 쉬움
  - AWS CodeBuild, Cloud Build : 퍼블릭 클라우드에서 제공하는 자체빌드 완전관리형 서비스
- CD : 지속적 배포 담당
  - Jenkins X : 쿠버네티스를 위한 젠킨스
  - Spinnaker : 넷플릭스에서 개발한 오래된 CD 도구, 멀티 클라우드 아답터 역할, UI 강점, 무거움
  - Tekton : 쿠버네티스 전용 네이티브 프레임워크. GCP 친화적
  - argo : Spinnaker 경량화
  - AWS CodeDeploy : AWS App 배포를 자동화
- Container Registry : 컨테이너의 버저닝을 중점적으로 관리
  - Docker hub : 가장 유명하고 큰 컨테이너 공유 플랫폼
  - Nexus : Private Repo에서 많이 사용하는 Repo 매니저
  - ECR, GCR : 퍼블릭 클라우드의 서비스

## 설계

- 배포 패턴 : 모놀릭, Service per VM, Container, Serverless
  - 모놀릭 : Multiple Service per host
  - Service per VM : 각 서비스가 VM 이미지로 패키징되고 VM 상에서 1개당 1개 서비스로 독립적 동작
    - OS 포함되어 사이즈가 크고 느리지만 AutoScaling등의 기능도 충분히 기능
  - Container : 컨테이너 이미지를 패키지화 하고 배포하고 k8s등으로 관리가능(러닝커브 발생)
    - 가볍고 빠른 배포
  - Serverless : 인프라 구축없이 소스만 구축. 서버, VM, 컨테이너등에 고민하지 않고 App 개발에 집중.
    - 퍼블릭 클라우드의 사용량 비례 금액 발생. 추적이 힘듬
- 브랜치 전략
  - Git-Flow : Master, Release, Develop, Feature, hotfix 브랜치를 적절히 운용 배치.
  - Github-Flow : 버그기능, 기능개발을 전부 Master에서 분기
  - No-Flow : 1개의 브랜치로 모든 작업을 합니다.
  - Two 브랜치 : Dev -> Master로 운용하고 Config Server나 환경변수 설정이 동반됨
  - Three 브랜치 : 품질을 중시
- 배포기법
  - 롤링 업데이트 : 서버를 1대씩 구버전에서 새버전으로 교체 배포. 구성이 단순.
  - 블루/그린 : 새로운 버전을 배포하고 혼재 없이 일제히 전환. 운영환경이나 무중단. 공존시간 없음.
  - 카나리 : 1대 내지 특정 유저에게만 배포했다가 문제 없을 경우 서서히 배포. 난이도 높음. 무중단 가능.
- Pipeline : 하나의 데이터 처리단계 출력이 다음 단계의 입력으로 이어지는 연결된 구조
  - 소스/스크립트
    - stages : 파이프라인 시작
    - stage('이름') : 파이프라인 단계 구분
    - step : 단계별 실행 스탭
- Dockerfile : Docker Image를 만들기 위한 설정 파일
  - 레이어를 적고 그걸 기준으로 이미지를 생성 (하단 단순 예시)

    ```dockerfile
      FROM ubuntu:14.04                    # 베이스 이미지 : 태그
      RUN mkdir -p /app                    # 이미지 생성전 수행 쉘 명령어
      WORKDIR /app                         # CMD에서 설정한 실행 파일이 실행할 디렉토리
      ADD ./app                            # 파일을 이미지에 추가
      RUN apt-get update
      RUN apt-get install apache2
      RUN service apache2 start   
      VOLUME ["/data", "/var/log/httpd"]   # 볼륨 추가. 디렉토리 내용을 컨터에너가 아닌 호스트에 저장
      EXPOSE                               # 외부노출 포트 정보
      CMD ["/app/log.backup.sh"]           # 컨테이너 시작시 실행하는 파일이나 스크립트
    ```

- Kubernetes : 컨테이너화된 App을 자동으로 배포, 스케일링 및 관리해주는 오픈소스 시스템
  - yaml 파일로 설정하고 spec을 기술하고 container 상태를 유지하게 함
- Terraform : 인프라스트럭쳐를 코드로 관리하기 위한 오픈소스도구
  - 클라우드 인프라스트럭처를 프로그래밍 언어로 정의하고 배포/vm 생성
  - .tf 파일로 필요내용을 코드로 관리

    ```shell
    terraform init # 테라폼 실행에 앞서 필요한 파일 다운로드
    terraform plan # apply전 변경 리소스 체크
    terraform apply  # 변경 정보 확인 > yes 입력시 CSP 자원 생성/변경
    ```
