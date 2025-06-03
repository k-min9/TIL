# AI Coding

- 개요 : AI를 이용한 코드 추천으로 생산성을 높여보자.
- 주요기능
  - 코드 제안 및 완성
  - 테스트 코드 작성
  - 소스 코드 언어 간 변환
  - 샘플 데이터 생성

## Copilot

- openAI 사에서 개발한 AI 기반의 코딩 도우미
  - Github 기반
- 환경 : VS Code (+Extension) + Github 연계
- 단축키
  - 제안 변경 : Alt + [, Alt + ]
  - 제안 수락 : Tab
  - 10개 제안 보기 : Ctrl+Enter
- Copilot-X :  GPT-4 기반 레벨업 버전, 24.04 기준 베타
  - 채팅 기반, 목소리 질문, CLI 자연어 입력 등
  - 사용 예시
    - Copilot-chat : 코드 물어보고 현재 커서에 붙여넣기, 코드 블록선택하고 /expain등으로 해석하기 /fix로 고치기
    - Copilot-CLI : gh copilot sugget "하고 싶은 일", gh copilot explain "설명 받고 싶은 내용", 후속 revise
    - Copilot-Voice : 음성으로 IDE 제어, 코드 작성 (active 모드 활성화로, copilot 안 불러도 됨)

## ChatGPT

- 프롬프트 엔지니어링
- 코드 분석
- 주석 제공
- 코드 문서화
- Pull Request 룰에 맞춘 Description 작성
  - 기존 코드와의 차이점, 구현된 유저 스토리...

## 기타

- Notation
  - 고스트 텍스트 : 코드 제안 항목
- 결국 사람이 확인을 해야한다.
  - Ctrl+Z, Ctrl+Y 등을 활용하여 기존 코드와의 환경을 해주자.
