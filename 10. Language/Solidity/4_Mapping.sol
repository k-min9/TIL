// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.7.0 <0.9.0;


// map 자료구조와 흡사, 키를 얻는 법은 제공하지 않음
contract Mapping {
    // mapping(기준키 => 값)
    mapping(address => uint) public addrToUint;

    // 키로 값을 가져오기
    function get(address _addr) public view returns (uint) {
        return addrToUint[_addr];
    }

    // 키로 값을 세팅
    function set(address _addr, uint _i) public {
        addrToUint[_addr] = _i;
    }

    // 값을 초기화 (지우는 것 아님)
    function reset(address _addr) public {
        delete addrToUint[_addr];
    }
}