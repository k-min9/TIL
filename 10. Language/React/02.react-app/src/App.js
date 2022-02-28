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
  // state 만들기, component 생성시 constructor가 가장 먼저 실행되어 초기화 담당
  constructor(props) {
    super(props);
    this.state = {
      subject: {
        title: 'State_WEB',
        sub: 'State_sub 내용물'
      },
      contents: [
        {id:1, title: '1번요소', desc: '1번 요소 설명'},
        {id:2, title: '2번요소', desc: '2번 요소 설명'},
        {id:3, title: '3번요소', desc: '3번 요소 설명'},
      ]
    }
  }



  render() {
    return (
      <div className="App">
        <Subject title = "WEB2" sub="prop는 이런식으로 하는겁니다."></Subject> 
        <Subject title = {this.state.subject.title} sub={this.state.subject.sub}></Subject> 
        <TOC data={this.state.contents}></TOC>
        Hello, React!!!
      </div>
    );
  }
}

export default App;
