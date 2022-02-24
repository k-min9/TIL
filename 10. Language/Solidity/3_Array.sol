// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

// 배열
contract Array {
    // 동적 배열
    uint[] public arr; // 선언만 할 경우, 초기화 없음
    uint[] public arr2 = [1, 2, 3]; // 선언 + 할당
    // 고정 배열, 초기값 0, 함수 내에서 로컬변수로 사용시 고정길이로만 선언해야함
    uint[10] public fixedSizeArr;

    // Compare with accessing state variable
    function get(uint i) public view returns (uint) {
        return arr2[i];
    }

    // push : element 추가
    function push(uint i) public {
        arr.push(i);
    }

    // pop : 마지막 element 지우기
    function pop() public {
        arr.pop();
    }

    // 지워지는게 아니라 초기화됨
    function remove(uint index) public {
        delete arr[index];
    }

    // returns the length of array.
    function getLength() public view returns (uint) {
        return arr.length;
    }

    // returns the entire array.
    function getArr() public view returns (uint[] memory) {
        return arr;
    }

    function createArray() external pure returns (uint[] memory){
        // 함수 내에서 로컬변수로 사용시 고정길이로만 선언해야함
        uint[] memory a = new uint[](5);
        return a;
    }
}
