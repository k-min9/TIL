# Agile

- User Story Hierarchy : Theme > Epic > (User) Stories > Task
  - XP User Story = Product Backlog(Scrum 용어) = 사용자 요구사항(기능목록)
    - 작성의 3요소 : Scope(범위), Importance(중요도), Estimation(예측)
      - 앞면 : A로서 B하기 위해 C하기를 원함 / 뒷면 : Acceptance Criteira(확인 조건)
      - 다음 공정(Sprint, Itertation) 시작 전까지 빠르게 식별하며 진화하는 요구사항에 대응
    - INVEST 원칙 : User Story 원칙
      - Independent : 독립적
      - Negotiable : 협상가능한
      - Valuable : 사용자와 고객에 가치있는
      - Estimable : 추정가능한
      - Small : 작은
      - Testable : 테스트 가능한
    - 우선순위 정의 : 기능타입, 가치 순으로 정의
      - 중요도가 높은 User Story는 중요도가 모두 달라야함
    - Story Point : 사용자 스토리 사이즈를 피보나치 수열을 이용하여 상대적인 값으로 Estimate
      - 종래의 Function Point(공수)와는 다름

- Planning
  - Release # : 몇번째 배포에서 추가될 기능인지
  - Sprint Goal : 구체적으로 직관적으로 Sprint 마무리 단계에서 구현되어야 되는 내용을 표현
  - User Story를 중요도에 따라 정렬하고 팀 추정 속도를 고려하여 Sprint에 할당
    - User Story Mapping : 릴리스계획을 시각적으로 표현. X축에 시간흐름 Y축에 우선순위
  - Task 도출
  - DOR(Definition of Ready) : 개발준비
    - 예시 : 사용자 정의 명확, INVEST, User Story Clear...
  - DOD(Definition of Done) : 완료
    - 예시 : 단위테스트 통과, 코드리뷰 완료, 인수기준 충족, 동료검토 완료...
  - Sprint Review
    - 좋은 Demo로 끝내면 Scrum에 큰효과를 가져오고 좋은 Feedback을 가져옴
  - Sprint 회고

- 기타
  - MVP(Minimum Value Product) : 최소실행 가능한 제품
  - MMP(Minimum Market Product) : 마케팅할 수 있는 가장 작은 기능 세트
    - 더 적을수록 좋다는 철학에 기반한 제품 개발 전략
  - CRC 모델링 : Class + Responsibility + Collaboration
    - 큰 디자인 틀 + 풀어야 할 문제 + 객체가 의지하는 Service와 control
