// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.7.0 <0.9.0;

contract Struct {

    // 할 일 구조체(Struct)
    struct Todo {
        string text;  // 제목
        bool completed;  // 수행여부
    }

    // 구조체 배열 -> public 선언시 get 함수는 자동 생성 해 줌
    Todo[] public todos;

    // create : 할 일 추가
    function create(string memory _text) public {
        todos.push(Todo(_text, false));
    }

    // update : 할 일 제목 수정 (해당 번호 할 일의 제목 수정)
    function update(uint _index, string memory _text) public {
        Todo storage todo = todos[_index];
        todo.text = _text;
    }

    // toggle : 할 일 완료 여부 변경
    function toggle(uint _index) public {
        Todo storage todo = todos[_index];
        todo.completed = !todo.completed;
    }

    // get : 할 일의 상세 정보
    function get(uint _index) public view returns (string memory text, bool completed) {
        Todo storage todo = todos[_index];
        return (todo.text, todo.completed);
    }
}
