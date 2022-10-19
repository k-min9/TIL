# 네트워크

## 00. 기본 - 기초 학습

기본 자료 : <https://www.youtube.com/playlist?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi>

## 01. AWS Certified Advanced Networking

네트워크 솔루션 설계 및 구현 분야에 5년의 실무 경험을 바탕으로 복잡한 네트워킹 작업을 수행하는 개인을 대상으로 하는 시험

## 요약

- TCP (Transmission Control Protocol)
  - 연결지향형 프로토콜, 안정적으로, 순서대로, 에러 없이 교환하는 것을 도움
  - UDP보다 안전하지만 느리다. (구분될정도로 압도적으로 느리지는 않다.)
  - 통신과정

- 3-Way handshake : 연결과 송수신
  - 연결 수립 과정(연결 수립을 위한 통신)  
    TCP를 이용한 데이터 통신을 할 때 프로세스와 프로세스를 연결하기 위해 가장 먼저 수행되는 과정
    1. 클라이언트가 서버에게 요청 패킷을 보냄 (SYNC)
    2. 서버가 클라이언트의 요청을 받아들이는 패킷을 보냄 (SYNC + ACK)
    3. 클라이언트가 최종적으로 이를 수락하는 패킷을 보냄 (ACK)
  - 데이터 송수신 과정
    - 보낸 쪽에서 또 보낼 때는 ACK번호, SEQ 번호 유지
    - 받는 쪽에서의 SEQ 번호는 받은 ACK 번호
    - 받는 쪽에서의 ACK 번호는 받은 SEQ 번호 + 데이터 크기
- 4-Way handshake : 연결 종료
  - 연결 종료 과정
    1. 클라이언트에서 서버로 FIN+ACK
    2. 서버에서 응용에 해당 요청 전달하며,  
       클라이언트로 ACK 보냄(1 요청에 대한 응답) + 클라이언트로 FIN+ACK 보냄 (서버로부터의 요청)
    3. 클라이언트에서 서버로 ACK 보냄
- UDP (User/ Universal Datagram Protocol)
  - 비연결지향형 프로토콜, 안전한 연결을 지향하지 않음.
  - 전송방식이 너무 단순, 신뢰성이 낮고, 중복되거나 통보없이 누락되기도 함(순서 변경, 분실 오류 가능성 있음)
    - 오류의 검사와 수정이 필요 없는 프로그램에서 수행
  - 구조 (8바이트) : Source Port(2) + Destination Port(2) + Length(2) + Checksum(2)
    최소 20바이트인 TCP보다 작고, 통신 과부하가 적다. 실시간 처리나, 시간이 민감할 때 사용
  - UDP 프로토콜을 사용하는 대표적 프로그램
    - DNS 서버 : 도메인 물을때 IP 알려주는 서버
    - tftp 서버 : UDP로 파일 설정
    - RIP 서버 : 라우팅끼리 정보를 공유하고 설정하는데 사용하는 서버
    - 그 외 : DHCP, SNMP...

- HTTP 쓰는 이유
- 개요 : 요즘 자주 쓰는 버전은 HTTP/1.1 기반
- 배경
  - 상태 유지(Stateful)면 중간에 다른 서버(점원)로 바뀌면 안됨 > 무상태(Stateless)면 그 걱정이 없음
    - 무상태면 서버 교체나 장애 대응, 수평확장에 유리하다
      - 보완 기술 : 쿠키, 세션, 토큰
  - 연결성이면 1천명이 접속하고 있으면 1천개의 연결이 필요한데 1천명이 기껏해야 동시에 하는 요청은 수십건 정도
    - 트래픽이나 큰 규모의 서비스에서 한계가 뚜렷이 보임
- Websocket : 실시간 상호작용을 위해 만들어진 스펙
  - http는 TCP를 기반으로 한 프로토콜이고 Websocket도 그런 프로토콜 중 하나
  - stomp는 Websocket 위에서 동작하는 서브 프로토콜
    - websocket은 데이터 전송기술이지 규격이 없어서 규격이 있어야 해석이 쉬움
  - Flow
    - HTTP request를 통한 hand shaking으로 최초 접속
      - 동일한 포트 환경 + CORS나 인증 과정등을 동일하게 가져가갈 수 있음
    - 프론트에서 SockJS를 통하여 socket을 커넥트한다
      - sockjs = 쓰기 편하게 + websocket 미지원 브라우저 대응 기능
      - 스페셜 헤더를 사용하여 upgrade하고 nginx에서 이 사실을 받는다
        - Connection: Upgrade를 통해 http를 ws로 변환
    - 연결 이후 pub/sub 하여 이용한다.
    - 접속 종료의 Handshake 후 연결을 종료한다.
