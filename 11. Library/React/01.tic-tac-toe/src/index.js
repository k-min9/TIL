// From : https://ko.reactjs.org/tutorial/tutorial.html#before-we-start-the-tutorial
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

class Square extends React.Component {
  // state : 무언가를 기억하게 하는데 사용 => this.state로 구현
  // Square의 현재 값을 this.state에 저장하고 Square를 클릭하는 경우 변경
  // constructor(props) {
  //   super(props);
  //   this.state = {
  //     value: null,
  //   };
  // }
  // 이제는 props를 구축했으므로 필요 없어짐

  render() {
    // Props를 통해 Board로 부터 데이터 전달 받음
    return (
      // 상위로 부터 전달받은 props 이벤트에도 반응
      <button
        className="square"
        onClick={() => this.props.onClick()}
      >
        {this.props.value}
      </button>
    );
  }
}
// render 하나 밖에 없는 square은 함수 컴포넌트로 작성함으로써 빠르고 읽기 편해짐
// 결과는 아래와 같음
// function Square(props) {
//   return (
//     <button className="square" onClick={props.onClick}>
//       {props.value}
//     </button>
//   );
// }

class Board extends React.Component {
  // constructor(props) {
  //   super(props);
  //   // 초기값 설정 후 하위에 전달함으로써 O, X, null 세가지 상태만 가질 수 있음
  //   this.state = {
  //     squares: Array(9).fill(null),
  //     xIsNext: true,
  //   }
  // }

  renderSquare(i) {
    return (
    // Props를 통해 Square에 데이터 전달
    // 이제는 Game에게 전달 받기 때문에 state 에서 props로 전환
      <Square
        value={this.props.squares[i]}
        onClick={() => this.props.onClick(i)}
      />
    );
  }

  render() {
    // 승자 체크 및 게임 진행 안내 => 이것도 이제 game이 담당함
    // const winner = calculateWinner(this.state.squares);
    // let status;
    // if (winner) {
    //   status = 'Winner: ' + winner;
    // } else {
    //   status = 'Next player: ' + (this.state.xIsNext ? 'X' : 'O');
    // }

    return (
      <div>
        <div className="board-row">
          {this.renderSquare(0)}
          {this.renderSquare(1)}
          {this.renderSquare(2)}
        </div>
        <div className="board-row">
          {this.renderSquare(3)}
          {this.renderSquare(4)}
          {this.renderSquare(5)}
        </div>
        <div className="board-row">
          {this.renderSquare(6)}
          {this.renderSquare(7)}
          {this.renderSquare(8)}
        </div>
      </div>
    );
  }
}

class Game extends React.Component {
  // 시간 여행 추가를 위한 초기 state
  constructor(props) {
    super(props);
    this.state = {
      history: [{
        squares: Array(9).fill(null),
      }],
      stepNumber: 0,
      xIsNext: true,
    };
  }

  // 함수 정의 (renderSquare에서 사용)
  handleClick(i) {
    // 기존 배열을 수정하지 않고 slice 연산자로 사본 만들기 => 불변성
    // 불변성으로 얻을 수 있는 효과 : 재사용성, 회귀 가능, 이력 표기, 쉬운 변화감지...
    // const squares = this.state.squares.slice();
    const history = this.state.history.slice(0, this.state.stepNumber + 1);
    const current = history[history.length - 1];
    const squares = current.squares.slice();

    // 승리가 나거나 이미 채워져 있는 사각형 클릭할 경우
    if (calculateWinner(squares) || squares[i]) {
      return;
    }

    squares[i] = this.state.xIsNext ? 'X' : 'O';
    this.setState({
      // 배열은 push 보다 concat을 권장(기존 배열 변경이 적음)
      history: history.concat([{
        squares: squares,
      }]),
      stepNumber: history.length,
      xIsNext: !this.state.xIsNext,
    });
  }

  jumpTo(step) {
    this.setState({
      stepNumber: step,
      xIsNext: (step % 2) === 0,
    });
  }
  
  render() {
    const history = this.state.history;
    const current = history[this.state.stepNumber];
    const winner = calculateWinner(current.squares);

    // history map
    const moves = history.map((step, move) => {
      const desc = move ?
        'Go to move #' + move :
        'Go to game start';
      return (
        // 고유의 key는 필수! 명시적으로 전달
        <li key={move}>
          <button onClick={() => this.jumpTo(move)}>{desc}</button>
        </li>
      );
    });

    let status;
    if (winner) {
      status = 'Winner: ' + winner;
    } else {
      status = 'Next player: ' + (this.state.xIsNext ? 'X' : 'O');
    }

    return (
      <div className="game">
        <div className="game-board">
          <Board
            squares={current.squares}
            onClick={(i) => this.handleClick(i)}
          />
        </div>
        <div className="game-info">
          <div>{status}</div>
          <ol>{moves}</ol>
        </div>
      </div>
    );
  }
}

// 승자 판단 로직
function calculateWinner(squares) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}

// ========================================

ReactDOM.render(
  <Game />,
  document.getElementById('root')
);
