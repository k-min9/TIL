# React

## 개요

react는 UI 제작용 javascript Library. (Framework가 아님)
별도의 분류용 폴더를 생성할때까지는 Framework 폴더에서 관리

## Notation

- Component : 사용자 정의 태그
  - 가독성, 재사용성, 유지보수
  - props : component 내부로 보내는 data
  - state : props의 영향을 받아 component 내부에서 사용되는 것들

- Toolchain : 개발에 필요한 Tool 들을 한번에 제공

## 시작하기

1. 환경 설정

```
npm install -g create-react-app // -g : 어디서든 실행 가능
npm install -g serve // 배포용
```

2. react 환경 조성 원하는 폴더가서 create-react-app .

## 코드 작성

처음 보는 화면 index.html -> 기본 id가 root로 적혀있고, 내용은 src 폴더에서 관리
src폴더 속 index.js에서 확인 가능

```
ReactDOM.render(
    <App />  // App.js 호출
  document.getElementById('root')  // 기본 id
);
```

- 작성방식 : function, class 방식이 존재.

```
// function 방식
import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
    </div>
  );
}
```

```
// class 방식
import React, {Component} from 'react';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
      </div>
    )
  }
}
```

- css 코딩

```
App.js 내부에
import './App.css';
입력시, App.js import 시점에 css도 함께 로딩함
```

- 배포 & build

```
npm run build  // dist 생성
npx serve -s build  // 배포 (serve 설치 필수), build를 document root로 하겠다.
```

## 현재 상태 확인하기

구글 확장프로그램 : React Developer Tools 설치

- 현재 보는 컴포넌트의 내용이나 탭을 보거나 실시간으로 바꿀 수 있음
