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
