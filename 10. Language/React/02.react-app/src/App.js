import {Component} from 'react';
import TOC from "./components/TOC"  // 컴포넌트 분리
import './App.css';

// Subject라는 Component를 만들겠다.
class Subject extends Component {
  // render가 반환하는 것을 사용
  render() {
    return (
      // 단 하나의 최상위 태그로 시작해야 함
      <header>
        <h1>WEB</h1>
        <h2>{this.props.title}</h2>
        world wide web!
        <div>{this.props.sub}</div>
      </header>
    );
  }

}

// 컴포넌트 만들고 사용하기 + props(하위 컴포넌트로 data 보내기)
// 컴포넌트 분리하기 (TOC)
class App extends Component {
  render() {
    return (
      <div className="App">
        <Subject title = "WEB2" sub="prop는 이런식으로 하는겁니다."></Subject> 
        <Subject title = "WEB3" sub="prop는 이런식으로 하는겁니다.2"></Subject> 
        <TOC></TOC>
        Hello, React!!!
      </div>
    );
  }
}

export default App;
