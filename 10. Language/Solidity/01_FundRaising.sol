// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.7.0 <0.9.0;

// 모금 Contract
contract FundRaising {
    uint public constant MINIMUM_AMOUNT = 1e16;  // 상수, 최소 모금액 0.01 이더 (=1e16 wei)
    uint public fundRaisingCloses;  // 종료 시각
    address public beneficiary;  // 수령자(Fund 대상) 주소

    mapping(address => uint256) funderToAmount;  // 자료구조 map과 흡사하다는 것만 기억해두자. 각 모금자의 모금액을 저장해 둘 것임
    address[] funders;  // 모금자 주소 모음

    // 생성자
    constructor (uint _duration, address _beneficiary) {
        fundRaisingCloses = block.timestamp + _duration;  // block.timestamp : 현재 블록의 유닉스 타임스탬프 값
        beneficiary = _beneficiary;
    }

    // 1. 모금하기.
    // payable : 이더 이동이 있음, require : 유효성 체크함수, 조건 만족하지 못할 경우 진입 불가
    function fund() public payable {
        require(msg.value >= MINIMUM_AMOUNT, "MINIMUM_AMOUNT: 0.01 ether");  // msg.value : 보내진 트랜잭션에 보낸 값(이더)을 확인할 수 있는 전역변수
        require(block.timestamp < fundRaisingCloses, "FUND RAISING CLOSED");

        // 모금자를 저장
        addFunder(msg.sender);  // msg.value : 보낸 사람의 주소 값을 확인할 수 있는 전역변수
        funderToAmount[msg.sender] += msg.value;
    }


    function addFunder(address _funder) internal {
        if(funderToAmount[_funder] == 0 ) {
            funders.push(_funder);
        }
    }

    // 2. 현재 모금액을 확인하는 함수
    // view : 상태 변수에 변화를 가하지 않고 읽기만 하는 함수
    function currentCollection() public view returns(uint256) {
        if(address(this) == address(0)) return 0;
        return address(this).balance;  // this(이 사람)가 가지고 있는 balance(총 이더)의 양
    }

    // 수령자만 호출 가능
    modifier onlyBeneficiary() {
        require(msg.sender == beneficiary, "NOT BENEFICIARY ADDRESS");
        _;  // 필수 : 이 require 이후 이어서 계속 해라. 라는 뜻
    }

    // 모금 종료후에만 호출 가능
    modifier onlyAfterFundCloses {
        require(block.timestamp > fundRaisingCloses, "FUND NOT CLOSES YET");
        _;
    }

    // 3. 수령하기
    // 위에 있는 2개의 modifier 사용
    function withdraw() public payable
    onlyBeneficiary  
    onlyAfterFundCloses {
        // 컨트랙트 보유 이더(address(this).balance)를 요청 주소에게 송금
        // msg.sender.transfer(address(this).balance);  <<< 이거 안된다는데?
        payable(msg.sender).transfer(address(this).balance);
    }


    function selectRandomFunder() public view returns (address, uint256) {
        if(funders.length == 0) return (address(0), 0);

        // keccak256 내장 함수를 사용하여 모금자 주소 중 한명을 무작위로 반환
        bytes32 rand = keccak256(abi.encodePacked(blockhash(block.number)));
        address selected = (funders.length == 1 ) ? funders[0] : funders[uint(rand) % funders.length];
        return (selected, funderToAmount[selected]);
    }

}
