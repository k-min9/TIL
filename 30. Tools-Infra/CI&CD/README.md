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
