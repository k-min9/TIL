import {Component} from 'react';

// 기본 버전
// class TOC extends Component{
//   render() {
//     return (
//       <nav>
//         <ul>
//           <li>1. 1번요소</li>
//           <li>2. 2번요소</li>
//           <li>3. 3번요소</li>
//         </ul>
//       </nav>
//     )
//   }
// }

// App.js에서 state.contents를 주입받은 버전
class TOC extends Component{
  render() {
    var lists = [];
    var data = this.props.data;
    var i = 0;
    while (i < data.length) {
      // 내부적 unique 값인 key 부여 잊지 말 것
      lists.push(<li key={data[i].id}><a href={"/content/"+data[i].id}>{data[i].title}</a></li>);
      i = i + 1;
    }
    return (
      <nav>
        <ul>
          {lists}
        </ul>
      </nav>
    )
  }
}

export default TOC;