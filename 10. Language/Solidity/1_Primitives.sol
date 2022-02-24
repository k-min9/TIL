// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

// 상태 변수 기본 자료형
contract Primitives {

    // (기본값)을 가짐
    // 논리형
    bool public defaultBool; // (false)

    // 정수형
    uint public defaultUint; // (0)  unsigned 정수
    int public defaultInt; // (0)  signed 정수 : -8 ~ 256bit

    // 주소형 (이더리움 주소)
    address public defaultAddr; // (0x0000000000000000000000000000000000000000)
    string public defaultString; // ''

    // 주소 할당
    address public addr = 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4;

    /*
    uint의 규모 조절
        uint8   ranges from 0 to 2 ** 8 - 1
        uint16  ranges from 0 to 2 ** 16 - 1
        ...
        uint256 ranges from 0 to 2 ** 256 - 1
    uint 기본값 = uint256
    */
    uint8 public u8 = 1;
    uint public u = 123; 
    uint256 public u256 = 456;

    uint public maxUint = type(uint).max;
    uint public maxUint256 = type(uint256).max;

    /*
    일반 정수형 규모 조절

    int256 ranges from -2 ** 255 to 2 ** 255 - 1
    int128 ranges from -2 ** 127 to 2 ** 127 - 1
    */
    int8 public i8 = -1;
    int public i = -123; 
    int256 public i256 = 456;

    // 최소, 최대 확인
    int public minInt = type(int).min;
    int public maxInt = type(int).max;

    // 바이트형 : 데이터를 바이트 형태로 표현할 수 있음, 두 종류
    //- fixed-sized byte arrays: bytes#
    //- dynamically-sized byte arrays. byte[]
    bytes1 a = 0xb5; //  [10110101]
    bytes1 b = 0x56; //  [01010110]  
}
