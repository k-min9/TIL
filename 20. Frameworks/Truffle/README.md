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

- Metadata :  Metadata

- 오픈제펠린 : 블록 체인 및 소프트웨어 개발 회사로 표준 프레임워크와 플랫폼 제공
  
  ```
  npm install @openzeppelin/contracts
  ```

- 기타
  
  - operator : 특정 소유자의 토큰을 전송할 수 있는 모든 권한을 가지고, 토큰 소유자에서만 권한을 지정할 수 있음
  
  - emit : 준비된 Event를 발생시킴

## ERC-721

참조 : [ERC 721 - OpenZeppelin Docs](https://docs.openzeppelin.com/contracts/4.x/api/token/erc721)

- {IERC721}: 모든 호환 구현에 필요한 핵심 기능.

- {IERC721Metadata}: 이름, 기호(symbol) 및 토큰 URI를 추가하는 선택적 확장으로 거의 항상 포함됩니다.

- {ERC721}: 기본 URI 메커니즘이 있는 핵심 및 메타데이터 확장입니다.

- {IERC721Receiver}: safeTransferFrom를 통해 토큰을 수락하려는 경우 계약에 의해 구현되어야 하는 인터페이스

## Utils

참조 : [Utilities - OpenZeppelin Docs](https://docs.openzeppelin.com/contracts/4.x/api/utils)

### Address

### Context

### Strings