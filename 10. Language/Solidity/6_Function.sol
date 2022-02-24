// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.7.0 <0.9.0;

// Solidity의 특징적 함수
contract Function {

    uint public num = 1;

    uint public a = 1;
    string public s = "hello solidity";
    bool public b = true;

    // +1
    function addOne() public {
        num++;
    }

    // +x
    function addNumber(uint x) public returns (uint) {
        num += x;

        return num;
    }
 
    // view, pure : solidity 제공 함수
    // view - 순수하게 데이터를 접근해서 변경하지 않고 값만 가져옴(read) -> 가스 소모 없음 = 절약
    function addAndReturn(uint x) public view returns (uint) {
       return num + x;
    }

    // pure - 마찬가지로 상태변수에 접근하지 않는 함수
    function add(uint x, uint y) public pure returns (uint) {
       return x + y;
    }

    // Return many values
    function returnMany() public view returns (uint, string memory, bool) {
        return (a, s, b);
    }

}
