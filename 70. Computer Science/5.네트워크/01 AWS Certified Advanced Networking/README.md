# AWS Certified Advanced Networking

개요 : 네트워크 솔루션 설계 및 구현 분야에 5년의 실무 경험을 바탕으로 복잡한 네트워킹 작업을 수행하는 개인을 대상으로 하는 시험
목표 : VPC, NAT, Elastic Load Balancer, Cloud Front, Route 53, VPN, Direct Connect, Endpoint Service, Gateway 등 AWS에서 구현하고 운영하는 복합한 네트워킹 작업에 대해 이해하고, 실무에서 필요한 수준의 기술을 습득

- 방식
  - 타입 : 객관식. 170분 65문제
  - 목표 : 720점 이상
  - 범위
    - AWS를 사용하여 클라우드 기반 솔루션을 설계, 개발 및 배포
    - 기본적인 아키텍처 모범 사례에 따라 핵심 AWS 서비스 구현
    - 모든 AWS 서비스에 대한 네트워크 아키텍처 설계 및 유지 관리
    - 도구를 사용한 AWS 네트워킹 태스크 자동화

## 네트워크 기초 이론

- 네트워크 : 둘 이상의 컴퓨터(장비) 간의 데이터 통신을 위하여 서로 연결 시켜주는 기술
- 네트워크 장비
  - Network Interface Card (NIC)
    - 컴퓨터를 네트워크에 연결하여 통신하기 위한 장비
    - 모든 NIC에는 하드웨어 고유 식별 주소인 MAC ADDRESS가 부여 되어 있음
    - 그 외, 네트워크 어댑터, 네트워크 카드, 랜 카드, 이더넷 카드로도 불림
  - Switch : 장비를 연결하는 통신 장비.
    - MAC ADDRESS를 기반으로 통신을 하는 OSI Layer2 장비
  - Router : 최적의 네트워크 경로를 결정 하는 장비
    - IP 주소를 기반으로 통신을 하는 OSI Layer 3 장비
  - Firewall : 방화벽. 정의된 보안 규칙에 의해 들어오고 나가는 네트워크 트래픽을 제어하는 보안 장비
  - Access Point : 무선 장치들을 유선 네트워크에 연결하는 장비 (ex-공유기)
    - Wireless Controller(WLC) : 여러 Access Point를 관리하는 장비
- 네트워크 케이블
  - Ethernet : LAN에 사용되는 네트워크 모델
    - LAN의 국제적인 표준 규격인 IEEE 802.3 통신 규격
    - 속도 및 케이블의 물리적 종류에 따라 분류
    - 대부분 Copper(UTP)와 Optical Fiber 케이블을 사용
      - Copper(UTP, Unshielded Twisted Pair) 케이블
        - 구리선을 이용해 전기신호를 전달
          - RJ45 포트와 커넥터 사용
        - 전송 가능한 속도에 따라 CAT1 부터 CAT8까지 분류
        - 100m 내외 케이블 전송 거리, POE를 통한 네트워크 장치 전원 공급
      - Optical Fiber 케이블
        - 광섬유를 이용해 광선 신호를 전달.
          - 전송 중 전기 신호 간섭 업슴
        - 싱글/멀티 모드로 나뉘어 싱글 모드가 더 먼 거리(수십 km) 전송. UTP보다 빠름.
      - SFP 모듈 : 트랜시버, UTP 또는 Optical 케이블 연결을 위한 모듈식 슬롯(Hot swap).

## IP

- 개요 : 네트워크 통신을 하기 위해 각 장비에 부여하는 고유한 주소. 라우팅을 위해 필수
  - 분류 : IPv4, IPv6로 분류
- IPv4 : 32비트(0.0.0.0 ~ 255.255.255.255)로 43억개의 주소 부여 가능
  - CLASS : IP 주소의 효율적 사용을 위해 5개의 클래스(A~E)로 나눔
    - 네트워크 주소 + 호스트 주소
  - Subnetting : 주소 할당의 주소 공간 낭비를 막기 위해 IP 주소를 보다 작은 네트워크로 분할하는 작업
    - CIDR(Class Inter-Domain Routing) 방식 (/[네트워크 비트수])으로 세분화된 네트워크와 호스트 범위를 표현
    - 같은 네트워크의 호스트끼리만 통신 가능.
    - 다른 네트워크는 default 게이트웨이로 IP 패킷 전송
    - Subnet 계산 예시
      - 10.10.0.0/16
        - 앞의 '16'비트가 네트워크
          - Host Address Range : 10.10.0.1 ~ 10.10.255.254 (254)
          - Subnet Mask: 255.255.0.0
        - Subnet ID: 10.10.0.0 (이래서 range가 0.1부터 시작)
        - Broadcast Address: 10.10.255.255 (이래서 range가 .254로 끝남)
      - 192.168.0.0/30
        - 앞의 '30'비트가 네트워크
          - Host Address Range : 192.168.0.1 ~ 172.16.0.2 (2)
          - Subnet Mask: 255.255.255.252 (마지막이 11111100)
        - Subnet ID: 192.168.0.0
        - Broadcast Address: 192.168.0.3
  - Private IP Address vs. Public IP Address
    - Public IP는 인터넷에서 사용하는 IP주소로 중복되지 않고 고유하게 할당됨
    - Private IP는 기업, 개인의 내부망에서 사용하는 IP주소로 인터넷으로 라우팅이 안됨
      - IP 주소 자원을 절약할 수 있음
      - Private IP 사용 대역
        - 10.0.0.0 – 10.255.255.255 (10.0.0.0/8)
        - 172.16.0.0 – 172.31.255.255 (172.16.0.0/12)
        - 192.168.0.0 – 192.168.255.255 (192.168.0.0/16)
