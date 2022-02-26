// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.7.0 <0.9.0;

// 구조체 : 여러 자료형을 하나의 관점으로 묶어서 관리, 
contract Struct {

    struct MyStruct {
        string text;
        bool boolean;
    }

    // ARRAY, MAPPING으로 선언 가능
    MyStruct[] public structArray;

    // A mapping from address to Todo
    mapping(address => MyStruct) public addrToStruct;


    // 구조체 만드는 여러 방법 (다 같은 결과)
    // method 1 : 괄호형 방식
    function create1(string memory _text) public {
        structArray.push(MyStruct(_text, false));
    }

    // method 2 : json 타입 선언
    function create2(string memory _text) public {
        structArray.push(MyStruct({text: _text, boolean: false}));
    }
  
    // method 3 : 로컬 선언
    function create3(string memory _text) public {
        MyStruct memory s;
        s.text = _text;
        structArray.push(s);
    }

    // Update text
    function updateText(uint _index, string memory _text) public {
        MyStruct storage s = structArray[_index];
        s.text = _text;
    }

    // Switch Boolean
    function updateBoolean(uint _index) public {
        MyStruct storage s = structArray[_index];
        bool current = s.boolean;
        s.boolean = !current;
    }
}
