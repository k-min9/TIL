// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

// 접근 제어자 : Visibility ; private, internal, public, external
contract Parent {
    // State variables
    string private privateVar = "private variable";
    string internal internalVar = "internal variable";
    string public publicVar = "public variable";
    
    // Private function : 컴파일 해도 버튼식으로 직접 접근이 불가
    function privateFunc() private pure returns (string memory) {
        return "private function called";
    }

    // 이렇게 private func를 호출한다.
    function testPrivateFunc() public pure returns (string memory) {
        return privateFunc();
    }

    // Internal function : 자식(Child)에서 호출이 가능
    function internalFunc() internal pure returns (string memory) {
        return "internal function called in Parent Contract";
    }

    // 자식이 호출시 이게 작동
    function testInternalFunc() public pure virtual returns (string memory) {
        return internalFunc();
    }

    // Public functions
    function publicFunc() public pure returns (string memory) {
        return "public function called";
    }

    // External functions : 외부에서만 호출 가능
    function externalFunc() external pure returns (string memory) {
        return "external function called";
    }
}

contract Child is Parent {
    // Internal function call be called inside child contracts.
    function testInternalFunc() public pure override returns (string memory) {
        return internalFunc();
    }
}
