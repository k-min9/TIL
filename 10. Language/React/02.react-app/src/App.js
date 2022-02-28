import {Component} from 'react';
import TOC from "./components/TOC"  // 컴포넌트 분리
import Content from "./components/Content"  // 컴포넌트 분리
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
      mode : 'welcome',  // 현재 표시 화면 종류 추가
      subject: {
        title: 'State_WEB',
        sub: 'State_sub 내용물'
      },
      contents: [
        {id:1, title: '1번요소', desc: '1번 요소 설명'},
        {id:2, title: '2번요소', desc: '2번 요소 설명'},
        {id:3, title: '3번요소', desc: '3번 요소 설명'},
      ],
      welcome: {
        title: '안녕하세요!',
        desc : '반갑습니다.'
      }
    }
  }

  render() {
    var _title, _desc = null;
    if (this.state.mode === 'welcome') {
      _title = this.state.welcome.title;
      _desc = this.state.welcome.desc;
    } else if (this.state.mode === 'read') {
      _title = this.state.contents[0].title;
      _desc = this.state.contents[0].desc;
    }
    return (
      <div className="App">
        <Subject title = "WEB2" sub="prop는 이런식으로 하는겁니다."></Subject> 
        <Subject title = {this.state.subject.title} sub={this.state.subject.sub}></Subject> 
        <TOC data={this.state.contents}></TOC>

        {/* state 전환 버튼을 만들어보자 */}
        <h3><a href="/" onClick={function(e) {
          console.log(e)
          e.preventDefault(); // 페이지 전환등 원래 하려는 행동을 중지시킴
          // component 구성 후에는 setState로 바꿔야 render 함수가 호출된다.
          this.setState({ 
            mode:'read'
          });
          // bind로 this 주입
        }.bind(this)}>{this.state.subject.title}</a></h3>

        Hello, React!!!
        <Content title={_title} desc={_desc}></Content>
      </div>
    );
  }
}

export default App;
