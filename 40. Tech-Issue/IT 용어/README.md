# IT 용어

- 개요 : 쓰다가 헷갈리는 단축어나 자주 쓰이는 용어 모음

- IMDG(In-memory Datagrid)
  - 키워드 : 분산, 고가용성, 확장성, key-value, serializable
- IMDB(In-memory Database)

- 고가용성 : 오랜기간동안 정상 운영이 가능해지게 하는 성질 = 고장이 나지 않음 = 빠른 복구가 가능함
  - 복수의 서버를 운용함으로서 달성

- 핫 스왑(Hot Swap) : PC가 켜진 상태에서 장치의 플러그를 뽑고 안전하게 제거할 수 있음
- 핫 플러그(Hot Plug) : PC가 켜진 상태에서 장치를 제거하려면 반드시 컴퓨터를 종료해야 가능

- PDM(Product Data Management) : 설계 데이터 관리
- Product Factory : 상품 통합 관리 시스템
  - 키워드 : 표준화, 부품화

- Sharding : DB 분산 저장

- PoC : Proof of Concept, 기술 검증
- Pilot : 검증된 기술은 대규모 적용 전에 소규모로 진행
- BMT : BenchMarking Test, 성능 테스트

- 본 : CRUD 단일 액션 단위, 화면 갯수

- DRM : Digital Rights Management. 암호화 기술을 이용해서 비허가 사용자로부터 디지털 컨텐츠를 보호하게 하는 기술
- APM : Application Performance Monitoring. Application에 대한 성능정보 및 발생한 Error정보 그리고 Application이 동작중인 서버의 기본적인 Metric정보를 수집 할 수 있는 기능

- In-house : 내부개발

- 보상 트랜잭션 : 특정 작업이 실패했을 때 이전 작업 단계의 결과들을 실행 취소하기 위한 트랜잭션

- NAS(Network Attached Storage) : 네트워크로 통신하여 저장장치에 연결
  - TCP/IP와 같은 표준 네트워크로 Network Switch와 연결하여 사용
- SAN(Storage Area Networking) : 스토리지 전용 네트워킹. 대규모 네트워크 사용자를 위해 저장장치를 데이터 서버와 연결하여 별도의 네트워크로 관리하는 고속 네트워크 시스템
  - 개인이 일반적으로 사용하는 LAN선 대신에 광케이블(FC Cable)을 사용하는 것을 SAN의 표준으로 봄

- XML ( eXtensible Markup Language) : 확장될 수 있는 표시 언어.  HTML의 한계를 극복할 목적으로 만들어졌다.
  - 마크업 언어(HTML) 그 자체가 아니라 마크업 언어를 정의하기 위한 언어
  - 태그를 정의할 수 있다.
- POJO(Plain Old Java Object) : 단순한 자바 오브젝트. 객체 지향적인 원리에 충실하면서 환경과 기술에 종속되지 않고 필요에 따라 재활용될 수 있는 방식으로 설계된 오브젝트
  - 특징 : 특정 규약/환경에 종속되지 않음, 객체 지향적인 원리에 충실
  - 장점 : 깔끔한 코드, 테스트하기 좋음, 객체 지향적 설계
  - 예시 : 스프링

- AJAX(Asynchronous JavaScript and XML) : javaScript라이브러리 중 하나. JavaScript를 사용한 비동기 통신, 클라이언트와 서버간에 XML 데이터를 주고받는 기술

- WSDL(Web Services Description Language) : 웹 서비스 기술언어 또는 기술된 정의 파일의 총칭으로 XML로 기술된다.
웹 서비스의 구체적 내용이 기술되어 있어 서비스 제공 장소, 서비스 메시지 포맷, 프로토콜 등이 기술된다.
- SOAP(Simple Object Access Protocol) : 일반적으로 널리 알려진 HTTP, HTTPS, SMTP등을 사용하여 XML 기반의 메시지를 컴퓨터 네트워크 상에서 교환하는 형태의 프로토콜이다.
SOAP는 XML을 근간으로 헤더(선택사항, 메타 정보)와 바디(주요 정보)를 조합하는 디자인 패턴으로 설계되어 있다.

- IDC 이야기 : SK C&C 판교 데이터센터 화재 사건(2022.10.)
  - IDC : Internet Data Center
  - UPC : 무정전 전원 장치, IPC를 위한 보조 배터리
  - DR : Disaster Recovery, 재해 상태에서 복구
    - 서버 분산
    - 미러 구축
    - Fail-Over(시스템 대체 작동)용 스위칭 세컨드 서버 시스템
    - GSLB(Global Server Load Balancing) : 로드밸런싱이 아닌 DNS의 발전 기술
    - 배경 : DNS는 도메인이 들어왔을때 등록된 IP 중 하나를 반환
    - 문제 : DNS는 IP중 하나를 알고리즘(RR등)에 맞게 반환하는거지 네트워크 지연, 성능, 서비스 실패등을 고려하지는 않음
    - 추가 기능
      - 유저의 지역 정보를 파악 > 네트워크 근접성
      - 등록된 호스트들에 대한 Health Check > 사이트 부하 분산, 재해복구
