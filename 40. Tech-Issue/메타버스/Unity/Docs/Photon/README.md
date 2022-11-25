# Photon

## 개요

유니티 네트워크에서 사용하는 대중적인 네트워크 솔루션
4인 멀티 플레이어 게임 = 4개의 평행우주 => 제어해야 하는 캐릭터 수 : 4^2 = 16

## 추가 목표

- 대기방 (로비)
- 매치메이킹 시스템
- 채팅

## 개념

- 동기화
  - 로컬 : 사용자 근처에 물리적으로 존재, 주도권이 본인
  - 리모트 : 원격 접속을 통해 접근할 수 있는 존재, 주도권이 타인
- 서버 : 전용 서버, 리슨서버, P2P 서버
  - 포톤의 서버구성 : 전용 클라우드 서버(매치메이킹) + 로컬 서버

## 매치메이킹 서버

포톤은 매치매이킹에 전용 클라우드 서버를 제공함

- 룸 : 클라이언트가 모인 네트워크 상 가상 공간, 세션
  - 씬과의 차이 : 룸은 주파수가 같은 사람들를 공유하게 함, 씬은 물리적 장소
    - 같은 룸 다른 씬도 가능

## 권한

호스트 : 공정한 결과 보장과 수치 위변조 방지가 필요한 중요 연산 담당
클라이언트 : fx, 애니메이션 재생 등 기타 연산 담당

- RPC(Remote Procedure Call, 원격 프로시저 호출)를 사용
즉, 메서드나 처리를 네트워크를 넘어 다른 클라이언트에서 실행

## PUN(Photon Unity Network)

유니티용 포톤 네트워크 엔진

- 설치
  1. 어셋으로 PUN2 Free가 제공됨
  2. Window > Photon Unity Networking > PUN Wizard > Setup Project
  3. 이메일 입력시 자동 연동해줌, 그 후 Done의 Close 눌러서 종료

## 적용

포톤에서 모든 동기화는 PhotonView 컴포넌트에서 작업.
변수와 함수도 PhotonView 컴포넌트를 거쳐가야함

변수 동기화 : OnphotonSerializeView, 값이 자주 바뀌는 체력등에 활용
함수 동기화 : RPC
RaiseEvent : PhotonView를 거치지 않는 이벤트

## Photon View

네트워크상 식별자인 View ID를 부여
Observed Compnents List에 등록된 컴포넌트 들의 변화 수치 관측 
다른 버전의 자신의 동기화에 사용
IPunObservable 인터페이스 상속 컴포넌트만 관측 가능

## Photon Trasform View
자신의 게임 오브젝트에 추가된 트랜스폼 컴포넌트 값의 변화를 측정하고, Photon View를 사용하여 동기화

## Cinemachine
Package Manager에 준비되어있는것 설치하면 준비 끝