# 개요

- 블록체인 : 분산 컴퓨팅 기술 기반의 원장 관리 기술
  - 블록(데이터 저장 공간, 거래 기록도 저장) + 체인(연결)
  - 종류
    - 퍼블릭 : 공공, 개방형. 암호화폐를 통한 보상으로 운영.
      - 비트코인, 이더리움, 이오스
    - 프라이빗 : 폐쇄형. 관계자의 승인이 있어야 참여 가능. 암호화폐가 필요 없지만 발행은 가능
      - 하이퍼레저
    - 컨소시엄 : 퍼블릭과 프라이빗의 중간. 하나의 기관이 관리하는 프라이빗과 다르게 다수 참여자의 협의가 필요한 분야에서 효율적
- 트랜잭션 처리 과정 : 거래 발생 > 신 트랜잭션 > 네트워크내 모든 노드에게 공유 > 검증 실행 > 블록에 담겨 체인에 추가
- 채굴 : 트랜잭션을 모아 하나의 블록으로 만드는 과정. 보상으로 코인이 주어짐
- 역사
  - 비트코인 : 신뢰가 아닌 암호화 증명에 기반한 전자 결제 시스템, 직접 거래가 가능한 암호 화폐
  - 이더리움 : 거래기록만 남길 수 있는 비트코인의 한계를 극복하여 데이터를 저장하고 프로그램을 실행
- 생태계
  - DApp(Decentralized Application) : 이더리움, 이오스 같은 블록체인 플랫폼 네트워크 상에서 작동하는 탈중앙화 분산 App
    - 오픈소스로 누구나 참여할 수 있음
  - BApp(Blockchain App) : 카카오가 클레이튼 메인넷과 함께 선언한 용어
    - 운용주체가 존재하고 이들이 중앙에서 검증하는 구조인 프라이빗 블록체인, 일부만 참여
- 토큰 : 화폐 대용, 보상의 수단으로 지급되는 경우가 많음
  - 주차 토큰, 도서 상품권, 마일리지, 치킨집 쿠폰
  - 생태계의 지속적인 확장을 담당
- 블록체인에서의 토큰
  - 이더리움 중심으로 표준화
  - 종류
    - Fungible : 대체(교환) 가능, ERC-20
      - 돈, 같은 가치
    - Non-Fungible : 대체 분ㄹ가능, ERC-721
      - MVP 싸인 카드, 고유한 가치
      - 대표 프로젝트 : CryptoKitties
- vs 코인
  - 예전 만큼 큰 차이는 없고 경계선이 모호해짐
    - 코인은 거래소에서 사고팔 수 있는게 제일 큰 특징
    - 토큰도 거래소가 등장하고 회계 단위나 가치 저장, 이전이 편해짐
  - 명확한 차이점
    - 코인은 독립된 블록체인 네트워크에서 운영됨
      - 다른 플랫폼에 종속되어 있지 않음(비트코인, 리플)
      - 자체 메인넷을 가지고 독립적인 생태계를 구성(이더리움, 이오스)
      - 표준화가 되어있지 않음, 자체 블록체인 네트워크가 필요하고 개인이 만들기가 힘듬
      - ex) 이더리움 네트워크의 이더, 클레이튼 네트워크의 클레이
    - 토큰은 디앱이나 비앱안에 쓰여서, 생태계 확장에 쓰임
      - 이더리움에서 표준화(ERC) 되어 가이드라인을 따라하면 나만의 토큰을 만들기 쉬움
      - 기타) EOS, QTUM은 예전에 토큰이었지만 독립된 블록체인 네트워크를 개발하고 코인이 됨 > 토큰 스왑이라고 함
- 개발을 위한 자금 모집
  - ICO(Initial Coin Offering) : 유틸리티 토큰
    - 비앱내의 상품 또는 서비스 구매
    - 법적인 규제가 없음, 투자자가 보호받지 못함, 진입 장벽이 낮아 신속한 일처리 및 자율성
    - 비슷한 개념) 싸이월드의 도토리, 방문자가 많아지면 가치가 높아질 수 있음
  - STO(Security Token Offering) : 시큐리티 토큰
    - 자산을 소유한다는 개념
    - 의사 결정이 블록체인 상에서의 투표로 이루어지고, 많이 소유할 수록 권한이 커짐
    - 법적인 규제가 있고, 법률이 정한 증권 발행 절차를 준수, 투자자들이 법적으로 보호됨, 진입 장벽 높음
    - 비슷한 개념) 주식, 이익이 날때마다 배당금 지급
- EIP(Ethereum Improvement Proposal) : 이더리움 개선안, 유저들이 제안서 내는 곳
  - 종류와 주제
    - Standard Track EIP : 코어, 네트워킹, 인터페이스, ERC
    - Information EIP : 디자인 이슈, 가이드라인
    - Meta EIP : 절차, 개발도구 변경, 의사결정 방안
  - ERC(Ethereum Request for Comment) : 토큰 표준화 제안 형식
    - 기준을 정하는 이유
      - 비교적 토큰을 빨리 만들 수 있음
      - 함수가 표준화 되어있으니 외부(지갑, 거래소)에서 쉽게 호환 가능
    - ex) ERC-721 Non-Fungible Token Standard

## ERC-721 구현

- 언어 : Solidity 사용
  - TIL > 10. Language > Solidity 에서 기본적인 문법 학습 가능
- 계정 만들기 : <https://baobab.wallet.klaytn.foundation/>
  - 만든 계정에 Faucet으로 돈 받기
- EIP 공식 깃허브에서 [ERC-721 Specification](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-721.md) 읽고 복사

  ``` Solidity
  // ERC-721 인터페이스에서 구현해야 할 함수
  interface ERC721 {
    event Transfer(address indexed _from, address indexed _to, uint256 indexed _tokenId);
    event Approval(address indexed _owner, address indexed _approved, uint256 indexed _tokenId);
    event ApprovalForAll(address indexed _owner, address indexed _operator, bool _approved);

    function balanceOf(address _owner) external view returns (uint256);
    function ownerOf(uint256 _tokenId) external view returns (address);
    function safeTransferFrom(address _from, address _to, uint256 _tokenId, bytes data) public;
    function safeTransferFrom(address _from, address _to, uint256 _tokenId) public;
    function transferFrom(address _from, address _to, uint256 _tokenId) external payable;
    function approve(address _approved, uint256 _tokenId) external payable;
    function setApprovalForAll(address _operator, bool _approved) external;
    function getApproved(uint256 _tokenId) external view returns (address);
    function isApprovedForAll(address _owner, address _operator) external view returns (bool);
  }

  // 토큰 안전 전송(safeTransferFrom)을 위해 구현해야할 함수
  interface ERC721TokenReceiver {
    // external -> public으로 변경
    function onERC721Received(address _operator, address _from, uint256 _tokenId, bytes _data) public returns(bytes4);
  }
  ```

- ERC-721 인터페이스를 상속하여 구현

  ``` Solidity
  contract ERC721Impl is ERC721 {
    // mapping은 자료구조 map과 유사
    mapping (uint256 => address) tokenOwner;  // tokenId 입력시 토큰 주인 지갑 주소 리턴
    mapping (address => uint256) ownedTokensCount;  // 주소 입력시 보유 토큰 수 리턴
    mapping (uint256 => address) tokenApprovals;   // tokenId 입력시 토큰 전송 승인 권한 가진 지갑 주소 리턴
    mapping (address => mapping(address => bool)) operatorApprovals;  // 누가 누구에게 권한을 부여했는가를 저장

    fuction mint(address _to, uint _tokenId) public {
      tokenOwner[_tokenId] = _to;  // mapping tokenOwner 에 map
      ownedTokensCount[_to] += 1;
    }

    // balanceOf : 해당 계정 토큰 소유 갯수
    function balanceOf(address _owner) public view returns (uint256) {
      return ownedTokensCount[_owner];
    }

     // ownerOf : 해당 토큰 소유자의 address
    function ownerOf(address _tokenId) public view returns (address) {
      return tokenOwner[_tokenId];
    }

    // safeTransferFrom : 토큰 안전 전송, ERC721 호환성을 체크하여 토큰 유실을 방지
    function safeTransferFrom(address _from, address _to, uint256 _tokenId) public {
      transferFrom(_from, _to, _tokenId)

      // 받는 사람 계정이 Contract 계정인지 확인
      if (isContract(_to)) {
        // 토큰을 받을 수 있는 Contract 인지 확인 
        // [ERC721TokenReceiver] 인터페이스의 onERC721Received 확인
        // [ERC721TokenReceiver]를 구현했을 뿐인데 Auction인지 확인을 안함
        bytes4 returnValue = ERC721TokenReceiver(_to).onERC721Received(msg.sender, _from, _tokenId, '');
        require(returnValue == 0x150b7a02, "리턴값이 ERC721Received의 magic value가 아님");
      }
    }

    // safeTransferFrom 보조 함수 : Contract 계정인지 확인
    function isContract(address _addr) private view returns (bool) {
      uint256 size;  // size가 0이면 일반 계정, 0보다 크면 contract 계정
      assembly {size := extcodesize(_addr)}
      return size >0;
    }

    // safeTransferFrom : 토큰 안전전송 2. 위의 safeTransferFrom에서 매개변수만 하나 추가
    function safeTransferFrom(address _from, address _to, uint256 _tokenId, bytes data) {
      transferFrom(_from, _to, _tokenId)

      // 받는 사람 계정이 Contract 계정인지 확인
      if (isContract(_to)) {
        // 토큰을 받을 수 있는 Contract 인지 확인 
        // [ERC721TokenReceiver] 인터페이스의 onERC721Received 확인
        // [ERC721TokenReceiver]를 구현했을 뿐인데 Auction인지 확인을 안함
        // 위에서 '' 처리 한 부분에 data가 들어가 onERC721Received의 비지니스 로직에 쓰임
        bytes4 returnValue = ERC721TokenReceiver(_to).onERC721Received(msg.sender, _from, _tokenId, data);  
        require(returnValue == 0x150b7a02, "리턴값이 ERC721Received의 magic value가 아님");
      }  
    }

    // transferFrom : 토큰 전송
    function transferFrom(address _from, address _to, uint256 _tokenId) public {
      address owner = ownerOf(_tokenId)

      // 유효성 검사
      require(msg.sender == owner || 
      msg.sender == getApproved(_tokenId) || 
      isApprovedForAll(owner, msg.sender),  
      "보내는 사람이 토큰 주인이 아니며 전송권한이 없음");
      require(_from != address(0), "보내는 사람의 주소가 비어있음");
      require(_to != address(0), "받는 사람의 주소가 비어있음");

      ownedTokensCount[_from] -= 1;
      tokenOwner[_tokenId] = address(0);

      ownedTokensCount[_to] += 1;
      tokenOwner[_tokenId] = _to;
    }

    // approve : 토큰 승인, 제 3자가 해당 코인을 다룰 수 있게 전송 권한 계정을 넘김
    function approve(address _approved, uint256 _tokenId) public {
      address owner = ownerOf(_tokenId);
      require(_apperoved != owner, "토큰 주인과 받는 사람이 같으면 안됩니다.")
      require(msg.sender == owner, "토큰 주인만 권한을 이용할 수 있습니다.")
      tokenApprovals[_tokenId] = _approved
    }

    // setApprovalForAll : 토큰 전체 승인, 계정이 소유한 모든 토큰의 권한 이양
    // @_operator : 모든 토큰을 대신 운영해 줄 계정
    // @_approved : 권한 부여 여부
    function setApprovalForAll(address _operator, bool _approved) external {
      require(_apperoved != owner, "권한 부여자와 관리자가 같으면 안됩니다.")

      operatorApprovals[msg.sender][_operator] = _approved;
    }

    // getApproved : 해당 토큰의 전송권한이 있는 주소를 리턴
    function getApproved(uint256 _tokenId) external view returns (address) {
      return tokenApprovals[_tokenId];
    }

    // isApprovedForAll : owner가 operator에게 권한을 주었는지 확인
    function isApprovedForAll(address _owner, address _operator) external view returns (bool) {
      return operatorApprovals[_owner][_operator]; 
    }
  }

  // SafeTransfer를 위한 ERC721TokenReceiver 인터페이스 구현체 이름은 적당히 지어도 알아서 가져옴
  contract Auction is ERC721TokenReceiver {
    function onERC721Received(address _operator, address _from, uint256 _tokenId, bytes _data) public returns(bytes4); {
      // 비지니스 로직에 맞게 식별하는 함수...

      // 문제 없을 경우 식별자값 리턴
      return bytes4(keccak256("onERC721Received(address,address,uint256,bytes)"))
    }
  }
  ```

## 기타

- ERC
  - 20 : Fungible Token Standard
  - 165 : Contract가 어떤 interface를 상속받는지 확인
  - 721 : Non-Fungible Token Standard
- Notation
  - magic value : 기대한 값
- 디지털 서명(signature, 시그내쳐) : 첨단 기술로 보안이 강화된 전자 서명의 한 종류. 비대칭 암호화 이용
  - 블록체인에 기록되는 데이터의 보안 및 무결성을 보장하는 주요 측면 중 하나
    - 거래 내역을 암호화하고 내용과 함께 서명에 사용된 개인키와 공개키를 함께 전송
    - 수신자는 거래 내용과 함께 수신된 공개키로 내용을 열어 거래 내용의 원본과 동일한지 비교, 동일하다면 공개키 주인이 보낸 것
    - 블록체인의 모든 거래 정보에는 디지털 서명이 포함되어 있어서 거래 정보를 신뢰할 수 있음
    - 소유자, 주소, 거래 내역등의 기록이 저장되어 절대 훼손되지 않고, 원본임을 증명하는 역할을 함
- 스마트 컨트랙트 : 계약 당사자가 특정 조건으로 하는 코드를 블록체인에 담아두고, 조건이 만족되었을때 동작하는 계약
  - 트랜잭션 : 블록체인에서 이루어지는 모든 활동
    - GAS : 트랜잭션 활동 중 발생할 수 있는 수수료
- 블록체인 트릴레마 : 탈중앙성, 보안성, 확장성 중에 최대 두 개만 이룰 수 있는 상황
  - 확장성 : 네트워크의 규모가 커지면서, 트랜잭션을 얼마나 빠르게 처리할 수 있는가?
    - 탈중앙화에 대한 타협: 거래를 검토하는 엔터티의 수 줄이기
    - 보안에 대한 타협: 네트워크의 난이도 감소를 요구하는 블록 타임의 감소
  - 탈중앙화 : 중앙집권화된 서버로 운영되는 것이 아닌, 소규모 노드 간 자율적으로 운영되는 것
    - 합의(Consensus)를 통해 의사결정. 중개자의 역할이 사라지고 더 많은 사람들에게 이익을 분배할 수 있는 구조가 됨.
    - 분산화 할 수록 네트워크 속도 감소...
  - 보안 : 데이터나 프로그램에 대한 보호. 악의적 접근을 막는 행위
    - 노드 수가 부족하고 해시율이 낮아지면 해킹 위험이 큼
    - 노드 수를 위한 더 많은 자원 투자가 필요
  - 예시
    - 탈중앙성 + 보안성 : 검증 노드 수를 늘림 -> 속도가 느려짐
      - 비트코인(7TPS, Transaction per sec), 이더리움 2.0이전(20TPS)
    - 보안성 + 확장성 : 검증 노드 수를 줄임 -> 블록 생성자의 권한이 급격히 성장
      - EOS : 위임지분증명(DPoS) 합의 알고리즘으로 21명의 블록생성자만이 운영을 맡음
      - 하이퍼레저 : 프라이빗 블록체인, 기업 중심 개발, 채굴 방식을 특정 숫자 노드로 극히 제한하여 성능 향상
    - 탈중앙성 + 확장성 : 검증 노드 수를 줄임 -> 보안성이 낮아짐
- 샤딩 : 이더리움 트랜잭션 처리속도 증가를 위한 기술, 지분 증명의 검증자를 소규모 그룹(샤드)으로 분리해 각 그룹이 서로 다른 이더리움 트랜잭션을 동시다발적으로 처리하는 방식
