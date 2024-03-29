# 데이터 모델링

- 학습 목표
  - 데이터 모델링의 개념을 이해하고 수행
  - 데이터 모델링의 작업절차 이해
  - 데이터 모델링의 기본 구성요소와 기본가이드를 이해
  - 현행 시스템의 데이터 모델을 이해하고 TO-BE 개선 데이터 모델을 구성할 수 있다.
- 데이터 모델링 : 고객 비지니스 이해 > 논리ERD 도출 > 물리ERD 전환
  - 논리 데이터 모델 : 일반용어, 업무중심 모델 정의, 업무흐름 파악, 커뮤니케이션
    - 대상 : Entity, Attribute, Identifier, Occurrence
  - 물리 데이터 모델 : DBMS적합용어, 성능 중심, 파티셔닝 수행, 집계테이블 도출
    - 대상 : Table, Column, Primary Key, Row, Index

## 논리 데이터 모델링

- 데이터 분석 : 엔터티를 도출하고 속성/식별자/관계를 정의
- 논리 데이터 모델 : (기술적 구현과는 독립적으로) 고객 비즈니스의 관련 정보를 업무 관점에서 표현한 모델
  - 정규화를 통해 무결성/일관성을 유지
  - 절차 : 주제영역정의 > 엔터티 정의 > 관계 정의 > 식별자 정의 > 속성 정의 > 세부사항 정의
  - 산출물 : 주제영역정의서 > 엔터티정의서 > 논리ERD > 용어사전, 도메인정의서 > 속성정의서

### 절차

- 주제 영역(Subject Area) : 데이터 최상위 집합. 관심 기능/주요 토픽에 대한 엔터티 그룹
- 엔터티 : 정보를 저장하고 관리하기 위한 것. 영속적으로 존재하는 Occurrence(=인스턴스)의 집합 단위
  - 체크 : 식별자, 속성, 명명규칙, 유형(중심,독립,의존,특성,연관), 슈퍼-서브타입(세분화,배타/포함관계)
  - 엔터티 정의서, Information Enginerring 표기법
- 관계 : 엔터티 간 상호적 의미. 단, 엔터티 혼자서 스스로 관계를 가질 수 있음
  - 3요소 : Membership(관점), Cardinality(다중성), Optionality
  - 관계 정련 : M:M관계해소, 1:M자기참고관계, Arc관계, 역할에 따른 병렬관계
- 식별자 : 엔터티 내 Occurrence를 구분할 수 있는 구분자. 데이터를 유일하게 식별할 수 있는 속성
  - PK, FK... >> 식별자 관계(실선), 비식별자관계(점선)
  - 유일성, 최소성, Not Null, Never Change
- 속성 : 엔터티에서 관리하고 싶은 분리되지 않는 최소 데이터 단위
  - 개발단계까지 지속 진행하므로 논리 데이터 모델링 단계에서 완벽히 찾을 필요는 없음
  - 용어 사전 작성으로 동의어, 유의어등의 속성명 통일(예정:=예상)
  - 분류
    - 기본(Basic) : 기본속성
    - 설계(Designed) : 업무 필요 정보를 위해 시스템 자체고안. 코드류
    - 파생(Derived) : 다른속성에 영향을 받음. 계산식, 금액총합, 이자... > 검증규칙
- 세부사항 정의
  - 정규화 : 데이터 모델의 구조화와 개선화 절차. 중복된 데이터가 없도록 하는 것이 목적
    - 입력, 수정, 삭제 이상현상 제거
    - 함수의 종속성[결정자(주민번호) -> 종속자(이름, 주소)] 이용
    - 단계 : 1차>2차>3차>보이스코드>4차>5차
      - 도부이겨다줘 : 도메인,부분함수종속제거,이행종속관계제거,결정자가모두후보키,다치종속성제거,조인종속성만족
- 상관 모델링 : 정보화 시스템 구축을 위해 데이터에 대한 프로세스와 프로세스에 영향 받는 데이터를 분석
  - 목적 : 프로세스 모델과 데이터 모델의 정합성 검증, 중복/누락 프로세스와 엔터티 도출
  - 산출물
    - CRUD매트릭스 : 단위 Process와 Entity가 발생하는 CRUD를 기재
    - DFD(Data Flow Diagram) : 데이터가 프로세스를 따라 흐르면서 변환되는 과정
    - 화면정의서 : 화면을 통해 데이터 모델의 엔터티, 속성 등을 도출
- 논리데이터모델 통합 : 일반적으로 데이터 모델러에 의해 수행되는 데이터모델 통합

## 물리 데이터 모델링

- 물리 데이터 모델링 : 논리 데이터 모델을 테이블 생성 가능한 물리 데이터 모델로 전환
  - 목적 : 논리 데이터 모델은 업무를 표현하는 것이 목적 > 성능 향상을 고려한 테이블 전환이 필요
  - 전환
    - 구성요소 > 관계형테이블
    - 엔터티, 속성 > 테이블, 컬럼
    - 주식별자, 외부식별자 > PK, FK
    - 슈퍼-서브타입 > 통합/분리결정 : 개별테이블 or 각 서브타입 or 통합테이블
    - 이력/채번/코드 테이블 도출
    - 반정규화 on 컬럼, 테이블, 관계

### 상세

- 반정규화 : 일반적으로 조회의 성능이 향상
  - 테이블 반정규화 : 집계 테이블, 수직/수평 분할
  - 컬럼 반정규화 : 중복쿨럼, 파생컬럼, 이력테이블 컬럼, 복합PK중 일부내용을 일반속성으로, 복구용 컬럼
  - 관계 반정규화 : 접근 경로 단축, 조인과 복잡한 SQL 구문 해결
- 이력/채번/코드 테이블
  - 이력 : 과거 상태 추적
    - 변경이력 : 불특정시점, 최종데이터 조회 위주 / 주문변경, 계약변경
    - 발생이력 : 특정시점, 시점별 조회 / 급여계산, 요금청구
    - 진행이력 : 중간시점 데이터 조회 / 공사진행, 접수진행
  - 채번 : 비지니스 특정 번호
    - 채번 테이블, 시퀀스 오브젝트, SQL문 이용
- 물리명 적용 : 용어사전을 근거로 논리데이터모델의 엔터티명과 속성명을 영문 테이블명 및 컬럼명으로 변경
  - 무결성 : 관계형 DB 모델에서 보장해야 하는 항목
    - Entity 무결성 : 데이터를 유일하게 하는 식별자가 있어야 하며 그 값은 Null이면 안됨
    - Referential(참조) 무결성 : 관계가 있는 두 엔터티간의 일관성을 유지해야 함.
      - 외부식별자에 값이 있으면 반드시 참조하는 엔터티의 주식별자 값이 존재해야 함
    - Domain 무결성 : 동일한 컬럼값은 일관된 제약을 가져야함. (상품명은 전부 문자)
- 성능 관점 : 적절하고 분별있는 정규화/반정규화

## 데이터 표준

- 개요 : 정보 시스템에서 사용하는 데이터 관련 요소에 대해 공통된 형식으로 정의하여 사용
  - 커뮤니케이션 오류 방지, 일관성과 정합성, 데이터의 품질 도모
  - 구성항목 : 단어(기본단어/분류어), 표준용어(조합단어), 도메인, 도메인 그룹, 데이터 타입(+길이)
    - 도메인을 제대로 적용하지 않을 경우, 형변환에 따른 성능저하 유발
    - NUMBER(5,2) : 저장가능 최대길이 소수포함 다섯자리, 소수점 세째자리에서 반올림 (1234.56 = 에러)
- 데이터 표준화 : 원칙을 수립하여 전사적으로 적용하고 지속적으로 관리하는 모든 활동
  - 단어, 도메인, 용어 표준화
  - 코드 표준화 : 코드 도메인의 오너십을 정하고, 취합한 코드 유효값의 통합 가능 여부를 검증하여 통합 관리
    - 오너십 : 소유권 내지 그러한 업무/주제영역
    - 유효값 유무 : 코드 숫자와 매칭되는 유효값 유무
- 데이터 품질 : 데이터 이용자의 만족을 충족시킬 수 있는 수준
  - 전략 : 정책 수립, 조직 구성
  - 프로세스 : 계획 > 정의 > 측정 > 분석 > 개선의 순환
    - DQI(Data Quality Indicator) : 데이터 품질기준
      - 완전성 : 누락이 없거나, 조건에 따른 필수
      - 유효성 : 적절한 범위, 날짜, 형식
      - 정확성 : 선후관계, 계산정확, 최신성
      - 유일성, 일관성
    - CTQ(Critical to Quality) : 핵심으로 관리할 품질항목
    - 프로파일링 : 룰/유형을 이용한 통계적 데이터품질 측정 방식
    - Business Rule : 비지니스 데이터 업무 규칙
    - DQMS : 데이터 품질 관리 시스템
- 데이터 전환 : AS-IS 시스템의 데이터를 TO-BE 시스템으로 이전
  - 테이블 매핑 정의서로 전환 대상 확정
  - 속성 매핑 정의서
  - 데이터 검증 항목/방법 정의
  - 검증 요건 정의서로 계수 검증
