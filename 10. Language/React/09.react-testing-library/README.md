# React Testing Library

React 컴포넌트에 대한 유지 관리가 가능한 테스트를 작성할 수 있음
내부 코드가 바뀌더라도 유지할 수 있는 테스트할 수 있게 하는 방법에 집중

설치

``` Shell
// 타입스크립트 버전 create-react-app
npx create-react-app [프로젝트 이름] --template typescript 

npm install --save-dev @testing-library/react
```

## 동작

- 주요 함수
  - render() : 대상을 테스트 DOM에 렌더링
  - fireEvent : 특정 이벤트를 발생 시킴
    - ex) fireEvent.change(name, { target: { value: "M9" } });
    - ex) fireEvent.click(btn)
  - expect(대상).함수 : 대상이 원하는 상태인지 체크
    - ex) expect(btn).toBeDisabled(); // 비활성화 상태인지
  - waitFor : 비동기 동작에 대한 결과를 대기
  - createMemoryHistory : 선언 객체에 history값을 배열로 저장
  - jest.mock : 테스트용 mock 객체 생성
    - ex) jest.mock('위치', () => {return function() {return {Data이름: () => {내용물}}}})

``` Shell
// 타입스크립트 버전 create-react-app
npm run test --[파일명.spec.확장자]
ex) npm run test --App.spec.tsx
```
