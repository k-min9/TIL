// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.7.0 <0.9.0;

// 조건문 : 익숙한 방식, pure만 조심
contract IfElse {
    function foo(uint x) public pure returns (uint) {
        if (x < 10) {
            return 0;
        } else if (x < 20) {
            return 1;
        } else {
            return 2;
        }
    }

    function ternary(uint _x) public pure returns (uint) {
        return _x < 10 ? 1 : 2;
    }
}

// 이더리움이 튜링 완전 머신이라고 불리는 이유 -> 루프문이 가능
// 블록체인은 이게 안되었다. 무한 루프 걸림 -> gas limit으로 루프문을 만들어냄
contract Loop {
    function loop1() public pure {
        for (uint i = 0; i < 10; i++) {
            if (i == 3) {
                continue;
            }
            if (i == 5) {
                break;
            }
        }
    }

    function loop2() public pure {
        uint i;
        while (i < 10) {
            i++;
        }
    }
}
