# Truffle

## 개요

Ethereum을 위한 개발 Framework



## Getting Started

- 설치 & 시작

```
npm i truffle -g  // 전역 설치
truffle init  // 해당 트러플 프로젝트 시작
```

- 폴더 해설
  
  - contracts : Solidity 로 작성한 스마트 컨트랙트 폴더, truffle compile 수행시 build 폴더가 생성되며 배포와 호출에 필요한 바이트코드 및 ABI가 들어있음
  
  - migrations : 컨트랙트 배포시, 파일명 앞 숫자의 오름차순으로 컨트랙트 배포
  
  - test : 테스트 배포. truffle test <파일이름>으로 단위 테스트 및 시나리오 테스트 진행가능

## Notation

- EIP : 표준규약
  
  - 20 : 대체가능한 표준 토큰, 스마트컨트랙트 표준 API 구현가능
  
  - 165 : 방법에 대한 표준, 인터페이스 확인 구현 후, 사용 시점 감지.
  
  - 721 : NFT(공유, 대체 불가  토큰)

- ERC(Ethereum Request for Comment) : 이더리움 RFC, 이더리움 표준이 될만한 내용, 토큰 계약 실시

- IERC : 토큰 계약 인터페이스, 가시성, 파라미터와 리턴 확보에 유리

- 오픈제펠린 : 블록 체인 및 소프트웨어 개발 회사로 표준 프레임워크와 플랫폼 제공
  
  ```
  npm install @openzeppelin/contracts
  ```
  
  