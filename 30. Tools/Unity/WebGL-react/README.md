# WebGL - react

## 개요

Build를 WebGL로 하면 웹 환경에서도 유니티 환경을 구축하고 상호작용 할 수 있다.
react 버전으로 기술하지만 vue도 크게 다르지는 않기 때문에 필요할 경우 갈음 할 수 있음
ref docs & install : <https://www.npmjs.com/package/react-unity-webgl>

## Getting Started

- 전제 :react 버전으로 기술

1. File > Build Setting으로 진입
2. Add Open Scenes로 빌드하려는 씬 선택
3. Build Settings에서 Platform을 WebGL로 설정
4. Development Build 체크하기
5. Build 하기
6. 지정한 폴더에 Build 폴더가 생성됨. public으로 이동
7. react 프로젝트 쪽에 package 설치

   ```
   // ex - 현재 제작 환경 2021.f
   npm install react-unity-webgl@8.x  # For Unity 2020 and 2021
   ```

## 적용

```
import React from "react";
import Unity, { UnityContext } from "react-unity-webgl";

const unityContext = new UnityContext({
  loaderUrl: "build/myunityapp.loader.js",
  dataUrl: "build/myunityapp.data",
  frameworkUrl: "build/myunityapp.framework.js",
  codeUrl: "build/myunityapp.wasm",
});

function App() {
  // 여기에 사이즈를 넣지 않으면, 자동으로 쪼그라드는 것을 볼 수 있음
  return <Unity unityContext={unityContext} />;
}
```
