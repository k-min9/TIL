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

## Router

- 개요 : 연결 가능한 네트워크 중에 최적의 경로를 결정하고 트래픽을 전달
목적지 네트워크로 가는 경로는 라우팅 테이블에 저장이 되며 라우터는 라우팅 테이블을 참조해 트래픽 전송
  - Destination + Target
- 분류
  - Static Routes : 관리자가 직접 경로를 설정
  - Dynamic Routes : 라우팅 프로토콜을 이용하여 라우팅 테이블을 자동으로 구성
  각자 자신이 가지고 있는 IP 등의 정보를 다른 라우터에 Advertise(광고)하고 경로 설정에 다른 광고를 참조
- Routing Protocol Types : 라우터 간의 정보를 동적으로 수행하여 패킷이 목적지까지 가는 경로를 결정해 주는 프로토콜

## VLAN (Virtual Area Network)

- 배경 : Subnet이 나뉜 곳에 파일을 보내기 위해 Broadcast Traffic을 보내면 성능 저하와 보안 이슈 발생
- 개요 : 논리적(가상)으로 분할 하는 기능
  - Broadcast Traffic을 동일한 VLAN에서만 전달하게 설정.
  - 물리적 장비는 스위치 하나만 필요하여 비용 절감
  - 불필요한 트래픽을 줄여 성능 향상 + 보안 향상
- 포트 설정
  - Access Port : 스위치 내 전달. 1개의 VLAN만 전달 가능.
  - Trunk Port : 스위치 끼리 전달. 여러 VLAN 전달 가능. 802.1q(Dot1Q) 표준 사용.
    - Dot1q(1EEE 802.1q) : Ethernet Frame(전달 단위)에는 VLAN 정보용 태그가 없음
      - 다른 스위치로 트래픽을 보낼때 여러 VLAN 정보가 포함된 Dot1Q Header Tag를 붙임
      - 같은 스위치(Host)로 보낼때 Dot1Q Tag를 제거하고 Access Port로 전달(Access Port는 VLAN 정보를 들고 있어서 태그가 불필요)

## AWS 글로벌 인프라

- 구성 : 리전 > 가용 영역 > 데이터센터 > 엣지네트워크
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

## AWS 가상 네트워크(VPC)

- 개요 : AWS 계정의 가상 네트워크. 블록사이즈 /16 ~ /28
  - Private : VPC(리전 단위)에 네트워크 환경을 지원하는 서비스
    - Public IP를 부여하고 Routing Table을 거쳐 Internet Gateway를 통해 인터넷과 통신
    - ex) EC2
  - Public Services : 외부에 위치하며 인터넷으로부터 액세스 가능
    - ex) S3, DynamoDB, WorkSpaces
- 구성
  - 기본 VPC : 계정 생성시 리전별로 자동으로 생성 됨 (/16)
    - VPC 안에 가용영역이 Subnet(/20)되어  
    NACL(Network access control list, Subnet레벨 방화벽)을 통해  
    Routing table을 거쳐  
    IGW (Internet Gateway)와 연결  
- Custom VPC 생성
  1. VPC 생성
      - CIDR 블록 사이즈(/16 ~ /28) 내에서 생성, 이후 범위 수정 불가
      - 퍼블릭 IP CIDR 생성시 이후 프라빗 IP CIDR 추가 불가
      - IPv6로 생성시 범위 지정은 필수가 아닌 옵션
      - 라우팅 테이블, DHCP, Prefix 리스트, NACL이 자동생성됨
  2. Subnet 생성 : VPC 선택 후, 가용영역 고르고 생성
      - CIDR 블록 사이즈(/16 ~ /28) 내에서 생성, VPC 블록 주소 내에서
        - CIDR 블록 주소 수정 불가, 삭제 후 새로 생성만 가능
      - 하나의 가용영역 지정
      - 다섯개의 주소를 AWS가 가져감
        - .0 : Network ID(Netmask)
        - .1 - Gateway
        - .2 - DNS
        - .3 – Reserved
        - .255 - Broadcast
  3. Routing Table 생성 : 라우팅 규칙을 통해 네트워크 트래픽 전송되는 위치를 결정
      - Subnet에 명시적으로 등록하지 않으면 기본 RT와 연결됨
        - 명시적 서브넷 연결 > 서브넷 연결 편집
      - Destination : 트래픽을 이동할 대상 IP 주소(대상 CIDR)의 범위
        - IPv4, IPv6
        - Prefix List : 관리형 접두사 목록. IP CIDR 범위를 미리 리스트로 만들어 둔 목록
      - Target : 타겟 주소 : 대상 트래픽 전송시 사용할 게이트웨이, 네트워크 인터페이스 또는 연결
        - local은 VPC 내부통신 라우팅
      - CIDR 블록 주소 수정 불가, 삭제 후 새로 생성만 가능
  4. IGW(Internet Gateway) 생성 : VPC와 인터넷 간에 통신을 할 수 있게 함
      - 퍼블릭 IPv4가 할당된 인스턴스에 대해 1:1 NAT(네트워크 주소 변환)을 수행
      - 라우팅 테이블의 Target(타겟 주소) 역할
        - 퍼블릭 서브넷 : IGW와 바로 연결(라우팅)
        - 프라이빗 서브넷 : IGW와 바로 연결되지 않음
      - 순서
      1. 인터넷 게이트웨이 생성
      2. 메뉴에서 확인(Detached). 우측 상단 작업 > VPC와 연결
      3. 연결할 VPC 선택 후 연결. 메뉴에서 확인 (Attached)
      4. 라우팅 테이블에서 생성된 igw와 연결
- 보안 그룹 vs NACL(Network Access Control List)
  - 보안 그룹 : 인스턴스 레벨
    - 인스턴스에 대한 인바운드 및 아웃바운드 트래픽을 제어하는 가상 방화벽 역할
      - 인바운드 규칙 : 들어오는 규칙. 다른 곳에서 그 인스턴스를 접속.
        - 생성 규칙 : 유형 - 소스 (어디로부터 오는지)
      - 아웃바운드 규칙 : 나가는 규칙. 그 인스턴스에서 다른 곳을 접속.
        - 생성 규칙 : 유형 - 대상
    - EC2 ENI와 연결, 최대 5개까지 연결 가능
    - 허용 규칙만 존재하고 거부 규칙은 없음
    - 연결 상태를 추적하는 상태저장 방화벽(Stateful Firewall)
    (= 인/아웃바운드 규칙과 상관없이 리턴 트래픽은 거부하지 않는다.)
    - 생성된 VPC 내에서만 사용 가능
    - 트래픽 허용 여부 결정하기 전에 모든 규칙을 평가
    - 인스턴스와 연결하는 경우에만 적용됨
  - NACL : 서브넷 레벨
    - 서브넷 내부와 외부의 트래픽을 제어하는 방화벽
    - 하나의 서브넷은 하나의 NACL만 연결 가능
      - 반대로 하나의 NACL은 여러 서브넷과 연결 가능
    - 허용, 거부 규칙 모두 지정 가능
    - 연결 상태를 추적하지 않는 상태비저장 방화벽(Stateless Firewall)
    (= 리턴 트래픽에 각각의 인/아웃바운드 규칙을 따름)
    - 트래픽 허용 여부 결정 시점에 번호가 가장 낮은 규칙부터 처리
    (= 번호 낮을 수록 우선순위가 높음)
    - 연결된 서브넷의 모든 인스턴스에 자동 적용됨
    - 이슈 :  EC2 웹서버 운영시 외부에서 Client가 접속 후 리턴 트래픽을 받을 때 NAT를 사용하므로 임시포트(ephemeral ports) 1024-65535를 사용
- NAT(Network Address Translation) : Private IP 주소를 Public IP 주소로 변환
  - 배경 : Private IP를 가진 인스턴스는 인터넷으로 트래픽을 어떻게 보내나?
  - 분류
    - NAT Instance : 사용자가 Public EC2에 NAT 기능을 구성하고 설치
      - 장 : NAT Gateway에 비해 더 많은 기능 구현 가능, 보안 그룹 적용 가능
        - ex) Squid Proxy 설정으로 특정 URL로만 액세스 제한(DNS Filtering) 가능
      - 단 : EC2 고장시 기능 동작을 안하게 됨
      - 이슈 : 사용시 EC2 ENI의 원본/대상확인(Source/Destination Check) 비활성화 해야함
      활성화시 원본/대상이 아니라 트래픽이 Drop됨
    - NAT Gateway : 원리는 비슷하지만 AWS에서 제공하고 관리하는 서비스
      - 장 : 고가용성, 대역폭 자동 확장
      - 단 : 사용자 추가 기능 구현 불가, 보안 그룹 적용 불가
      - 이슈 : Gateway로 쓸 Elastic IP를 지정해야 함.
      이때 단 하나의 Public 주소만 쓰게 되므로 포트를 통해 접속을 분산 함. 따라서, NACL 인바운드 트래픽에서 1024 - 65535 포트를 허용해야 트래픽을 수신할 수 있음
  - 이용시 발생하는 문제와 해결
    - 포트 할당 오류로 인한 실패 또는 연결오류(ErrorPortAllocation) 발생
      - 문제 : 55000건의 동시 접속 지원을 넘은 요청
      - 해결 : NAT Gateway를 추가해서 더 많은 접속을 지원
    - 인스턴스에서 인터넷에 액세스는 되지만 특정 시간 후 끊어짐
      - 문제 : NAT Gateway 연결이 X초 이상 유후일 경우 연결 시간이 초과됨
      - 해결 : EC2 인스턴스에서 X초 미만 값으로 TCP keepalive를 활성화
    - 프라이빗 서브넷의 인스턴스에서 NAT Gateway를 통해 대상에 연결할 때 일부 TCP연결은 성공하지만 일부는 실패하거나 시간초과
      - 문제 : 대상 엔드포인트가 조각난 TCP 패킷으로 응답하는게 원인
      NAT Gateway는 조각난 패킷(fragmented packets)을 지원하지 않음

## EC2 Networkinng

- EC2 생성
  - 실습
    - public EC2, private EC2 생성
      - public : 보안그룹 RDP 인바운드 연결
      - private : 보안그룹 all 트래픽 허용
    - [원격 데스크톱 연결]로 public EC2에 연결 후,
      - ID는 administrator
      - EC2 > 인스턴스 > 연결 > windows 암호 가져오기에 pem키를 넣어 암호 획득
    - public EC2에서 putty를 사용하여 private EC2를 호출해보자
- ENI(Elastic Network Interface) : 서버가 VPC를 통해 통신하기 위해 필요.
  - 인스턴스 생성시 자동으로 생성됨. 추가 생성+연결 가능.
    - Dual-Homed Instance : 2개의 네트워크 카드를 연결해 하나는 내부, 하나는 외부와 연결하는 구성
  - IP주소, MAC 주소 등이 부여 됨
  - 인스턴스에 연결되어 네트워크 통신
- 탄력적 IP(Elastic IP) : 인터넷에 연결 가능한 고정적(정적)인 퍼블릭 IP 주소
  - 설정 안할 경우, 인스턴스 재시작시 다른 IP로 재할당
  - 할당 후, 인스턴스와 연결하면 끝
- 네트워킹 성능 향상시키는 방법
  - 인스턴스 유형 선택시 네트워크 성능이 높은 유형 선택
  - 향상된 네트워킹(Enhanced Networking) 사용
    - 프리티어를 제외한 모든 인스턴스 유형이 지원
  - 인스턴스가 점보 프레임을 지원하는지 확인하고 9001 MTU(최대 전송 단위)를 설정
    - 더 큰 패킷을 보낼 수 있게 됨

## Load Balancer

- 개요 : 트래픽을 분산하는 서비스. AWS에서는 Elastic Load Balancer라고 호칭  
비정상 대상을 감지하면, 해당 대상으로 트래픽 라우팅을 중단하고  
대상이 다시 정상으로 감지되면 트래픽을 해당 대상으로 다시 라우팅  
  - 조건 : 서브넷당 사용가능 IP 주소가 최소 8개 필요 (권장 최소 CIDR 블록 /27 넷마스크)
- 종류 : 로드 밸런스 생성시 유형에 따라 선택
  - Application Load Balancer(Layer 7/HTTP, HTTPS)
    - HTTP Header Content를 사용해 라우팅 요청 처리
    - 웹 애플리케이션, 서비스에 적합
  - Network Load Balancer(Layer 4/TCP, UDP, TLS)
    - Protocol, Port Number를 사용해 라우팅 요청처리
    - ALB에 비해 상대적으로 빨라서 수백만의 대용량 트래픽 처리에 적합
  - Gateway Load Balancer(GWLB)
    - Layer 3 – Gateway Load Balancer Endpoint
    - Layer 4 – Gateway Load Balancer
    - GENEVE protocol을 사용하여 encapsulation 트래픽 전송
    - Transparency한 네트워크 게이트웨이를 제공하므로 방화벽, IPS, IDS 등의 원본 패킷의 데이터가 중요한 가상 어플라이언스에 적합
  - Classic Load Balancer(이전 세대, Layer 4 + Layer 7 / HTTP, HTTPS, TCP. TLS)
    - Protocol, Port Number를 사용해 라우팅 요청처리
    - 곧 deprecated 될 예정
- 구성 (GWLB)
  - Listener : 연결 요청을 확인하는 프로세스
    - 클라이언트/대상과 로드 밸런서 간의 연결을 위한 프로토콜 및 포트번호로 구성
  - Target Group : 대상(Target)의 모임
    - 대상 유형 : EC2 인스턴스, EC2 Auto Scaling Group, IP address, Lambda
    - 프로토콜
      - ALB : HTTP, HTTPS
      - NLB : TCP, TLS, UDP, TCP_UDP
      - GWLB : GENEVE
    - 상태 검사(Health Check) : 등록된 Target(대상)에게 상태 확인 메시지를 보내서 대상의 상태를 확인
      - 경로, 정상 임계값(X회 이상 연속 성공), 비정상 임계값(X회 이상 연속 실패), 제한 시간, 간격, 성공코드 설정
    - 속성
      - ALB : 등록 취소 지연(Deregistration delay), 느린 시작 기간(Slow start duration), 알고리즘, 고정(Stickness)
      - NLB : 등록 취소 지연, 등록 해제시 연결 종료, 고정, 프록시 프로토콜, 클라이언트 IP 주소 보존
- Application Load Balancer 상세
  - 최소 2개의 가용영역 지정
  - Listener Protocol로 HTTP, HTTPS 사용할 수 있음
    - HTTPS 프로토콜 사용시 SSL/TLS 인증서 배포 필요
      - 인증서는 ACM(AWS Certificate Manager)사용 또는 클라이언트 인증서 사용
  - 소스 IP 전달(Source IP Preservation)사용을 위해서는 X-Forwarded-For 헤더를 사용
  - WebSocket 기능 사용을 위해서는 Stickiness를 활성화 해야 함
  - Listener 규칙 : Host header, Path, Http header, Http request method, Quert string, source IP
- Network Load Balancer 상세 : 계층이 다르지 ALB와 유사
  - 수백만 유저(Millions of Concurrent Users/Requests Per Second) 의 경우에 적합
  - Listener Protocol로 TCP, TCP/UDP, UDP, TLS를 사용 할 수 있음
    - TLS 프로토콜 사용시 SSL/TLS 인증서 배포 필요
  - 고정 IP 주소 할당 가능
  - 클라이언트 IP 주소 전달 가능
  - Websocket 지원
  - Listener 규칙 설정 없음
- Gateway Load Balancer 상세 : ALB, NLB와 이질적
  - Gateway Load Balancer Endpoint: 서비스 공급자(Provider) VPC의 가상 어플라이언스와 서비스 소비자(Consumer) VPC의 애플리케이션 서버 간에 프라이빗 연결을 제공
  - 인터넷 게이트웨이를 통해 서비스 소비자 VPC로 들어오는 모든 트래픽은 먼저 검사를 위해 Gateway Load Balancer Endpoint 라우팅된 다음 Application Server로 라우팅
  - Application Server에서 나가는 모든 트래픽은 다시 인터넷으로 라우팅되기 전에 검사를 위해 Gateway Load Balancer 엔드포인트로 라우팅

## Cloud Front

- 개요 : 콘텐츠 전송 네트워크 서비스 (CDN, Contents Delivery Network)
- 특징 : 엣지 로케이션(전세계 200개 이상)의 캐싱 기능을 이용하여 콘텐츠를 글로벌 사용자에게 더 빨리 배포하도록 지원하는 서비스
- 생성 : Cloudfront > 배포 > 생성 ('동작'에서 차후 설정 변경 가능)
  - 뷰어 : 서비스 이용자, 프로토콜 정책(HTTP...), 접근 Method 설정 가능
  - 기본값 루트 객체 : 처음 접속시 들어가는 사이트 설정 가능
    - 첫 슬래시(/) 빼야함
- 보안 액세스
  - 뷰어 / 오리진 프로토콜 정책 : 뷰어 프로토콜, 오리진 프로토콜 정책으로 보안
    - Match Viewer(뷰어 일치) : 오리진 프로토콜이 뷰어 프로토콜의 정책을 따라 감
  - OAI(Origin Access Identity) : 오리진에 직접 접근을 막고 클라우드 프론트를 통해서만 할 수 있도록 설정
    - CloudFront가 Origin Access ID(원본 Access ID)를 가지고 Origin쪽 Policy에 OAI를 허용
      - 차후 생성된 OAI를 원본 편집으로 변경 가능
  - Singed URL, Signed Cookies : 서명된 URL또는 쿠키를 이용해서 콘텐츠에 접속하는 기능
    - URL또는 쿠키에는 콘텐츠만료기간, 액세스가능한 IP주소를 저장할 수 있음
    - URL은 1개 파일 1개 서명, Cookie는 1개 쿠키 여러 파일 접속 가능
  - 지역 제한(Geographic Restrictions) : 특정 국가에서의 엑세스 제한
  - AWS WAF(Web Application Firewall)와 연결하여 보안 강화
  - 사용자 지정 HTTP 헤더가 포함된 요청만 전달하도록 Application Load Balancer를 구성
  - 비대칭키 암호화 방법을 이용한 필드 레벨 암호화 사용 (시험범위 외)
- Lambda@Edge : AWS Lambda를 확장하여 CloudFront로 전달하고 엣지로케이션에서 해당 함수를 실행
  - AWS Lambda 서버리스 컴퓨팅 서비스
  - 다음과 같은 CloudFront 이벤트가 발생할 때 Lambda 함수를 실행
    - CloudFront가 최종 사용자의 요청을 수신할 때(최종 사용자 요청)
    - CloudFront가 오리진에 요청을 전달하기 전(오리진 요청)
    - CloudFront가 오리진의 응답을 수신할 때(오리진 응답)
    - CloudFront가 최종 사용자에게 응답을 반환하기 전(최종 사용자 응답)
  - 사용 예시
    - A/B 테스트를 위해 사이트의 다양한 버전을 볼 수 있도록 쿠키를 검사하고 URL을 다시 작성
    - User-Agent 헤더를 확인하여 사용 중인 디바이스를 기반으로 디바이스의 화면 크기에 따라 다른 이미지를 반환
    - 최종 사용자 요청 또는 오리진 요청 이벤트가 발생할 때 HTTP 응답을 생성
    - 헤더 또는 권한 부여 토큰을 검사하고, CloudFront가 오리진으로 요청을 전달하기 전에 헤더를 삽입하여 콘텐츠에 대한 액세스 권한을 제어
    - 외부 리소스에 대한 네트워크 호출을 생성하여 사용자 자격 증명을 확인하거나 추가 콘텐츠를 가져와 응답을 사용자 지정

## Route 53

- 개요 : AWS의 DNS 서비스
  - 퍼블릭 도메인 구매, 이전
  - AWS 내부 VPC에서 사용할 수 있는 프라이빗 도메인 생성
  - 라우팅 정책 적용
- DNS(Domain Name System) : 사람이 읽을 수 있는 도메인 이름을 컴퓨터가 읽을 수 있는 IP 주소로 변환하는 시스템
  - 레벨
    - FQDN(Fully Qualified Domain Name) : 전체 주소 도메인 네임
    - Root Domain : 도메인 맨 끝의 점(.), 생략 가능하고 보통 생략 되어 있음
    - TLD(Top Level Domain) : .com 같은 최상위 도메인. 도메인 네임의 가장 마지막 부분
    - SLD(Second Level Domain) : 그 부분을 제외한 부분
  - 레코드 유형 : DNS에 알려줄 트래픽을 도메인에 라우팅하는 방식
    - A : 도메인 네임을 IPv4 주소로 라우팅 (www.google.com -> 192.100.10.1)
    - AAAA - 도메인 네임을 IPv6 주소로 라우팅
    - CNAME - 도메인 네임을 도메인 네임으로 라우팅 (site.google.com -> blog.google.com)
    - ALIAS(별칭) - 도메인 네임을 AWS리소스로 라우팅 (www.google.com -> AWS EC2, ALB...). AWS 전용.
    - MX(Mail eXchanger) - 이메일 서버연동시 메일의 소유를 확인하기 위한 레코드
    - NS(Name Server) – DNS레코드를 가진 DNS 서버를 식별 하기 위한 레코드. 기본 생성
    - SOA(Start Of Authority) – 도메인의 정보와 권한을 가진 레코드. 기본 생성
  - DNS resolver(해석기) : 들어온 도메인 이름을 해석하는 중간자. 인터넷 서비스 제공업체(skt, kt 등...)에서 관리
    - 도메인 입력시 DNS Resolver로 라우팅
    - name 서버를 탑부터 순서대로 돌아가며 IP 주소 획득
      - 이때 DNS Resolver가 일정 기간 캐싱
      - 캐싱 기간은 TTL(Time to live, 단위 : 초)로 Route53이 IP 반환시 함께 부여
    - 얻은 IP 주소로 요청을 웹서버로 전송하고 반환받음
  - 라우팅 정책 : 레코드 생성시 선택 가능
    - 단순 라우팅(Simple) : 도메인 -> IP로 라우팅. 대상 IP가 여럿일 경우 랜덤
    - 가중치 기반(Weighted) : 서버에따라 분산하는 가중치를 설정하고 그것을 기준으로 라우팅
      - 트래픽 분산과 여러버전App 테스트에 유용
    - 지연 시간(Latency) : 가장 짧은 지연시간을 제공하는 리전으로 라우팅
    - 지리적 위치(Geo Location) : 속한 대륙이나 국가를 기준으로 라우팅
    - 장애 조치(Failover) : 레코드 유형 - 기본(Primary)라우팅이 실패하면 레코드 유형 - 보조(Secondary)로 자동 라우팅
      - 상태 검사 : 상태를 모니터링하고 상태가 좋지 않은 경우 장애조치가 작동
    - 다중값 응답 : Route53 DNS에서 다수의 값을 반환, 상태확인에 따라 정상인 IP 주소만 전달하고 대상은 랜덤한 주소 중 하나를 접속
- Route 53 Private Hosted DNS Zones : Amazon VPC 내에서 트래픽을 라우팅, 호스팅 영역이 프라이빗
  - 프라이빗 Domain Name을 프라이빗 IP 주소로 변환 하여 라우팅
  - 프라이빗 호스팅 영역을 VPC에서 사용하려면 VPC 설정의 DNS 호스트 이름(DNS Hostname)과 DNS 확인 (DNS Resolution)을 필수로 활성화 해야 함
    - Amazon에서 프라이빗 호스팅 영역에 대한 DNS 쿼리 제공
    - DNS Hostname : Custom VPC의 경우 이 옵션은 기본적으로 비활성화
    - DNS Resolution : VPC DNS 서버로부터의 DNS쿼리만 수락
      VPC DNS 서버의 IP 주소는 VPC IPv4 네트워크 범위를 기준으로 2를 더한 예약된 IP 주소(예, 10.1.0.2)

  - DHCP(Dynamic Host Configuration Protocol) : TCP/IP 네트워크 상의 호스트로 구성 정보를 전달하기 위한 표준을 제공
    - DHCP 옵션세트에 지정된 도메인 서버를 사용해 도메인 네임을 확인
- Route53 DNS Resolver for Hybrid Cloud : 추가 DNS 서버를 배포하지 않고도 Amazon VPC와 온-프레미스 데이터 센터간에 트래픽을 전달
  - 시나리오
    1. Private Hosted Zone은 Shared Service VPC와 연결
    2. Inbound Endpoint: 온-프레미스에서 확인하려는 Route 53 이름에 대한 온-프레미스 DNS 서
  버에 대한 전달 규칙(Conditional Forward)을 만듬
    3. Outbound Endpoint: AWS VPC에서 온-프레미스로 확인하려는 이름에 대한 Route 53 Resolver 규칙을 생성

## VPC Peering

- 배경 : VPC 간에는 기본적으로 네트워크 통신이 되지 않음
- 개요 : 두 VPC간에 트래픽을 라우팅할 수 있도록 네트워킹 연결
  - 퍼블릭 인터넷을 통과하지 않고 프라이빗 IP 주소를 사용하여 통신
- 구성
  1. 요청자가 다른 VPC와 피어링하기 위한 요청 생성
  2. 수락자 VPC의 소유자가 VPC 요청을 수락하여 피어링을 활성화
  3. 라우팅 테이블에 피어링을 타겟으로 하면 반대편 VPC가 연결되게 destination과 target을 각각 추가
- 주의 사항
  - IP 영역이 중첩되면 안됨
  - 전이적 피어링 불가
    - A과 B가 피어링, B와 C가 피어링일때 A가 B를 통해 C와 연결할 수 없음. 피어링은 1:1!
- VPC Peering DNS Resolution : 퍼블릭 IPv4 DNS 호스트 이름으로 접근시 퍼블릭이 아닌 프라이빗 IPv4 주소를 확인하도록 설정
- 공유 VPC : 여러 AWS 계정에서 애플리케이션 리소스를 중앙 관리형 공유
  - 공유 VPC와 개인의 VPC를 Peering connection
  - VPC 소유 계정은 동일한 조직에 속한 다른 계정과 한 개 또는 여러 개의 서브넷을 공유
    공유 참여자는 공유된 서브넷의 해당 애플리케이션 리소스에 CRUD를 행사할 수 있음

## VPC PrivateLink

- 개요 : VPC와 서비스 간에 프라이빗 연결을 제공하는 기술
- 서비스
  - VPC 엔드포인트 : 인터넷을 통하지 않고 AWS 서비스에 프라이빗하게 연결할 수 있는 VPC의 진입점
    - 동일한 리전에서만 지원
    - 종류
      - 게이트웨이 엔드포인트 : AWS S3와 DynamoDB에 대한 프라이빗 연결
      - 인터페이스 엔드포인트 : 그 외 서비스
        서브넷의 IP 주소 범위에서 프라이빗 IP 주소를 사용하는 탄력적 네트워크 인터페이스
      - Gateway Load Balancer 엔드포인트
  - VPC 엔드포인트 서비스(AWS PrivateLink, 동명) : VPC 내에 있는 애플리케이션 또는 서비스
    - 인터넷을 통하지 않고 AWS 내부 네트워크를 통한 트래픽
    - 다른 AWS 계정의 VPC Endpoint에서 엔드포인트 서비스(AWS PrivateLink)로 연결
      - 벤더(Service Provider)는 VPC에 애플리케이션을 구성하고 VPC Endpoint 서비스를 구성
      - 하나 또는 여러 고객(Consumer) AWS 계정의 VPC Endpoint가 벤더 (Provider) AWS 계정의 NLB 또는 GWLB에 연결
        - 고객이 많거나 고객 VPC의 IP 중복을 걱정하지 않아도 됨

## Hybrid Cloud and VPN

- VPN(Virtual Private Network, 가상 사설망)
  - 개요
  - 종류
    - Site-to-Site VPN : 다른 Site의 Private IP를 가질텐데 그 라우터 들을 인터넷을 통해 보안 터널링으로 연결, IPSec 암호화 프로토콜 사용
    - Client VPN : Client PC와 회사를 Private하게 연결, TLS 암호화 프로토콜 사용
  - 기타
    - IKE(Internet Key Exchange) : VPN간의 연결을 성립하기 위해 사용하는 암호화 키 관리 프로토콜
    - Hybrid Cloud : AWS Cloud와 외부 On-promise를 연결하기 위해 AWS가 제공하는 VPN 서비스
- AWS VPN
  - 연결 옵션
    - AWS Site-to-Site VPN (AWS Managed VPN) : AWS VPC와 온-프레미스와의 터널을 구성하여 연결, IPsec 프로토콜 사용
    - AWS Client VPN : AWS 리소스와 노트북 등의 클라이언트와 VPN연결, SSL/TLS 프로토콜 사용
      - VPC는 Client VPN Endpoint를 세팅
      - 클라이언트는 VPN 접속을 위한 VPN 구성 파일이 담긴 소프트웨어를 설치
      - Active Directory 등의 자격증명을 이용해 클라이언트가 VPN 연결 권한을 부여 받음
    - AWS VPN CloudHub : AWS VPC와 여러 곳의 온-프레미스를 연결하여 서로 통신할 수 있게 AWS Site-to-Site VPN을 구성
    (site-to-site VPN을 여러개 만들어 하나의 클라우드를 형성, on-promise가 다른 vpc 및 다른 on-promise와도 연결 가능)
    - Software Site-to-Site VPN : EC2인스턴스에 VPN 소프트웨어를 설치하여 VPN기능을 구현, 외부 프로그램인 만큼 자유롭게 설정이 가능하지만, 직접 관리해야 함
- AWS Site-to-Site VPN 상세
  - 개요 : IPSec 암호화 프로토콜을 사용 하여 AWS VPC와 온-프레미스간에 프라이빗 네트워크를 구성
  - VPC와 연결을 위한 Virtual Private Gateway +  
    온-프레미스의 Customer Gateway Device의 정보를 구성하기 위한 Customer Gateway를 설정하고  
    구성 파일을 다운 받아 고객 게이트웨이 디바이스(Customer Gateway Device, CGD, 라우터)에 설치 하여 VPN 연결 터널을 구성
  - AWS Direct Connect의 백업으로 사용 가능
  - VPN 터널당 최대 대역폭은 1.25Gbps
  - VPN 사용을 위해 UDP 500, IP Protocol 50을 방화벽에서 허용해야 함
    - Virtual Private Gateway (VGW) : AWS VPC와 온-프레미스 네트워크를 연결하는 라우터 역할
      - Site-to-Site VPN, Direct Connect 연결을 통해 온-프레미스와 연결
      - VPC는 하나의 VGW만 연결 가능하고 그 VGW를 통해 여러 외부 연결
      - VGW 생성시 ASN(Autonomous System Number)를 지정
        - Autonomous System은 내부 연결을 포함하여 하나의 관리자에 운용되는 네트워크 그룹
        - 인터넷에 연결되는 Public ASN과 내부적으로 사용되는 Private ASN로 나뉨
          - Private ASN 범위는 64512 ~ 65534이고, 디폴트 값은 64512
        - 외부 연결(Exterior gateway protocol)은 BGP(Border Gateway Protocol)를 사용하고 BGP끼리만 라우팅 교환
          - 교환에 내부 라우팅 등의 정보 알 필요가 없음
    - Customer Gateway : 온-프레미스의 고객 라우터의 설정 값을 AWS에 제공하는 게이트웨이
      - 물리적으로 설치 되는 것이 아닌 AWS에서 구성되는 가상 게이트 웨이
    - Customer Gateway Device(CGD) : 온-프레미스에 설치된 라우터 등의 물리적 디바이스 또는 소프트웨어 애플리케이션, AWS 콘솔에서 VPN 구성 파일을 받아 설치하면 VPN 연결 터널이 구성됨
  - VPN Tunnel
    - Site-to-Site VPN 연결에 2개의 터널 사용
    - 각 터널은 고유의 '가상 프라이빗 게이트웨이 퍼블릭 IP 주소'를 사용
    - 터널 하나가 사용 불가능하게 되면 네트워크 트래픽은 사용 가능한 터널로 자동으로 라우팅
    - 옵션(암호화, Dead Peer Detection(DPD) 시간 초과, IP 주소 등)을 사용자가 직접 지정 가능
- AWS Route Learning
  - 배경 : VPC와 온-프레미스는 서로 다른 네트워크를 어떻게 routing table을 학습하나?
  - 종류
    - Static Routing : 수동으로 직접 구성, 소규모에 적합
      - Site-to-Site VPN에서 지원
    - Dynamic Routing : 라우팅 프로토콜에서 연결된 라우터끼리 자동으로 공유, 대규모에 적합
      - Direct Connect, Site-to-Site VPN에서 지원
      - AWS에서는 Dynamin Routing시 BGP(Border Gateway Protocol)만 사용 가능. (= BGP Protocol)
        - 다른 자율 시스템(AS)의 라우터 간, 조직 외부에서 사용하는 Exterior Gateway Protocol
        - 서로 Peer 관계로 연결된 라우터끼리만 Network routes(prefix) 정보를 공유함
        - 라우팅 경로가 여럿일 경우 Best-Path 알고리즘 사용
          - 선택 순서
            1. Highest Weight
                - 값이 높은 것을 우선하여 선택
                - 자기 자신의 라우터는 기본값이 32768이며 다른 라우터에서 학습한 값은 0
            2. Highest Local Preference
                - 값이 높은 것을 우선하여 선택
                - 기본값은 100
            3. Shortest AS Path : 해당 네트워크에서 여기까지 오는데의 경로
                - 가장 짧은 경로를 우선하여 선택
                - 자기 자신의 라우터는 i (internal)이며 여러 라우터를 거칠 경우 AS Path가 추가 됨
                - 속도가 느려도 Path가 짧은것을 선택함.
                  - 조정 방법
                    - AS Path에 임의의 내용을 추가해 길게 만들어버리자(AS Prepending)
                    - Weight를 변경해서 조정하자.
            4. Lowest Metric
                - 값이 낮은 것을 우선하여 선택
                - 기본값은 0
        - TCP 179 프로토콜 사용
        - ASN으로 BGP 라우터를 구분
      - 라우트 전파(Route Propagation) : 자동으로 라우트를 추가하게 하는 옵션
    - 라우팅 테이블 겹치거나 일치하는 경우 : Local > Static > Dynamic중 구체적인 순서로 선택

## Direct Connect(DX)

- 개요 : AWS와 온-프레미스 간에 DX Location을 통한 전용선을 통해 프라이빗 네트워크 연결 생성
- 전용선 : Cloud - DX Location - On-promise를 각각 연결
  - Cloud - DX Location AWS Cage : AWS Backbone으로 연결, AWS가 관리
  - DX Connection 내 AWS Cage - Customer Cage : Cross-connect
  - Customer Cage - On-promise Router : WAN으로 연결, 고객 내지 통신사(Telco Partner) 등이 관리
- 특징
  - 포트당 1Gbps, 10Gbps, 100Gbps 연결 속도 사용 가능
  - 물리적인 구성을 해야 하기에 설치 시간이 오래 걸림
  - VPN보다 가격이 비싸며 인터넷을 통하지 않기에 인터넷 전송 비용이 들지 않음
  - 기본적으로 암호화를 지원하지 않음
    - 암호화를 위해 Direct Connect에 VPN을 구성 가능
  - 트래픽이 인터넷 연결을 사용하는 Site-to-Site VPN보다 안정적
  - 연결을 생성하기 위해 Virtual Interface (VIF)를 생성하고 VIF는 OSI Layer2 레벨로 통신하므로 각 VIF마다 VLAN을 지정하여 트래픽 분리
  - 고가용성과 복원력(Resiliency)을 고려한 옵션 지원
- 하드웨어 네트워크 요구사항
  - 각각의 포트에 맞는 트랜시버 사용이 필요
  - 포트에 대한 자동 협상을 비활성화(Disable auto-negotiation)
  - 단일 모드 광섬유(Single-mode fiber)를 사용
  - VLAN을 사용해야 하기 때문에, 802.1Q VLAN 캡슐화(802.1Q VLAN encapsulation)를 지원해야 함
  - Dynamic Protocol인 BGP Protocol을 사용하기 때문에 디바이스에서 BGP(Border Gateway Protocol)와 BGP MD5 인증을 지원해야 함
  - 기타 : 네트워크에 양방향 포워드 감지(BFD(Bidirectional Forwarding Detection))를 구성할 수 있음
    - 연결된 두 라우터 또는 스위치 간의 실패를 빠르게 감지(milli~microseconds)
  - 연결 방법
    - Dedicated Connection : 고객이 AWS 콘솔을 이용해 연결을 요청하고 구성하는 방법
    - Hosted Connection : AWS Direct Connect Partner가 고객 대신 연결을 요청하고 구성하는 방법
  - 순서
    1. 이름, DX Connection location 위치, 포트 속도, On-promise의 AWS DX 파트너 사용 여부, 공급자(Telco...) 입력하여 요청
    2. LOA-CFA(Letter of Authorization – Connecting Facility Assignment) 다운로드
          - DX 로케이션에서 고객 라우터를 AWS 라우터에 연결하는 권한이 적혀있음
          - 파트너 업체에 보내면 Cross-Connect 구성해줌
    3. 이 이후에 Virtual Interface (VIF)를 생성하고 사용할 수 있음
  - Ling Aggregation Group (LAG) : 여러 DX 연결을 LACP(Link Aggregation Control Protocol)를 사용하여 하나의 논리적인 인터페이스로 묶는 것
    - 합친 규모의 포트로 사용할 수 있으며, 하나의 링크에 문제가 생겨도 지속적 데이터 전송이 가능 (액티브 모드)
    - 최대 묶을 수 있는 링크 수 4
    - 같은 유형의 포트(1G, 10G 같이 동일한 대역폭)만 가능
- Virtual Interface (VIF)
  - 개요 : 물리적인 DX 연결이 OSI Layer 2이기 때문에 Layer 3를 사용하는 IP를 사용한 네트워크 전달을 위해서 가상인터페이스(Virtual Interface)를 사용
  - 유형
    - Private VIF : VPC와 연결된 1개의 VGW와 연결 또는 1개의 Direct Connect Gateway와 연결
      - Direct Connect 연결 당 최대 50개의 Private VIF 생성가능
      - Direct Connect Gateway : 가상 프라이빗 게이트웨이(VGW)와 프라이빗 가상 인터페이스(VIF)를 그룹화, 여러 리전에 있는 여러 VPC를 연결할 수 있음
        - 연결제한
          - 하나의 Private VIF는 최대 10개의 VGW와 함께 DX Gateway에 연결될 수 있음
          - 하나의 Transit VIF는 최대 3개의 Transit Gateway와 함께 DX Gateway에 연결될 수 있음
          - Direct Connect Gateway는 최대 30개의 Private VIF 또는 Transit VIF를 가질 수 있음
        - 트래픽 전송 제약
          - Direct Connect Gateway와 연결된 VPC에서 다른 VPC로의 전송 불가
          - Direct Connect Gateway와 연결된 하나의 VIF에서 다른 VIF로의 전송 불가
    - Public VIF : S3, Dynamo DB 등의 AWS 퍼블릭 서비스와 인터넷을 사용하지 않고 서비스 연결
      - Direct Connect 연결 당 최대 50개의 Public VIF 생성가능
    - Transit VIF : Transit Gateway와 연결, Direct Connect Gateway와 연결
      - Transit Gateway는 1:1 VPC Peering이 아닌 중앙 허브를 통해 각 VPC 또는 VPN간의 모든 트래픽 라우팅
  - VLAN : 하나의 DX 연결에 여러 VIF의 트래픽을 논리적으로 분리하기 위해 VLAN 사용
    - 각각의 전송은 VLAN 번호를 가짐
    - VLAN 전송을 위해 802.1q 트렁크 프로토콜을 사용
  - Direct Connect Routing : BGP(Border Gateway Protocol)를 사용, AWS Route Learning과 우선순위 선택 방식이 동일
    - Highest Weight >  Highest Local Preference > Shortest AS Path > Lowest Metric
    - BGP Community : Public VIF를 통해 광고되고 수신되는 라우팅을 제어함
      - BGP 커뮤니티 태그(DX routing의 속성값)를 사용해 라우팅이 전파 되는 범위를 지정 할 수 있음
        - 7224:8100 - 동일 리전
        - 7224:8200 - 동일 대륙
        - 태그 없음 - 모든 퍼블릭 AWS 리전

## 기타

- 테넌시 : 전용 하드웨어
- 퍼블릭 IP 자동 할당 : 다음 EC2에 자동으로 퍼블릭 IP를 할당함
- DNS 확인 : ON이어야 주소가 DNS 서버를 거쳐서 접속함
- 등록 취소 지연 : Auto Scaling 축소등으로 Deregistration 된 인스턴스에 더 이상 요청을 보내지 않도록 하는 기능
- 고정(Stickness) : 클라이언트가 세션을 유지한 상태라면 모든 요청을 동일한 인스턴스로 유지하는 기능
- 프로비저닝(Provisioning) : 사용자의 요구에 맞게 시스템 자원을 할당, 배치, 배포해 두었다가 필요 시 시스템을 즉시 사용할 수 있는 상태로 미리 준비해 두는 것
- 온 프로미스(On-promise) : IT 서비스를 운영하는 회사가 자체적으로 보유한 공간에 물리적으로 하드웨어 장비를 가지고 직접 운영하는 방식을 말합니다. 클라우드 컴퓨팅 기술이 나오기 전까지 일반적인 기업이 사용하던 일반적인 인프라 구축 방식
