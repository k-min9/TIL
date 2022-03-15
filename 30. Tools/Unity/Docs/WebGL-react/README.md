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

   ```markdown
   // ex - 현재 제작 환경 2021.2.14f1
   npm install react-unity-webgl@8.x  # For Unity 2020 and 2021
   ```

## 적용

```markdown
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

## React -> Unity

- react에서 send 함수를 사용함

  ```markdown
    function spawnEnemies() {
      // parameter : gameObjectName, methodName, parameter(string, number, boolean)
      unityContext.send("GameController", "SpawnEnemies", 100);
    }
  ```

- unity에서 public으로 해당 method를 만들어둬야 함

## Unity -> React

조금 더 복잡하므로 순서에 맞춰서 설명
ref docs 추가 :

1. Unity로 부터 제어하거나 정보를 받고 싶은 Component에 unityContext.on 사용

   ```markdown
   // unityContext.on("JSLib function", eventListner)
    unityContext.on("GetSpeed", function(speed) {
      SetSpeed(speed);  // 무언가 하고 싶은 js 동작
    });
   ```

2. JSLib 파일 만들어서, Unity Project Assets/Plugins/ 안에 배치
  JSLib : C#과 JS간의 모든 통신에 사용되는 파일

   ```markdown
   mergeInto(LibraryManager.library, {
      // "JSLib function 이름 : function(변수 이름만, ...)"
      GetSpeed: function (speed) {
        // window.dispatchReactUnityEvent(유니티 function 이름, parameters, ...)
        window.dispatchReactUnityEvent("GetSpeed", speed);
      },

      // 함수 추가...
    });
   ```

   - 추가 : String 전달시 Pointer_stringify(str) 사용

3. C# 코드 만들기

   ```C#
   // namespace import
    using UnityEngine;
    using System.Runtime.InteropServices;

    public class GameController : MonoBehaviour {
      // 내보내고 싶은 변수
      public float speed = 8f;  // 이동 속력

      // 클래스 내부 DLL import
      [DllImport("__Internal")]
      // 이름 JSLib 설정이름과 동일한지 체크
      private static extern void GetSpeed(float speed);  

      // 원하는 이벤트에 연계
      public void Start () {
    // 특정 환경에서만 구동하게 해둠 (개발 환경 고정시, 딱히 필요 없음)
    #if UNITY_WEBGL == true && UNITY_EDITOR == false
        // 위 함수 이름과 동일하고 parameter 맞는지 체크
        GetSpeed(speed);
    #endif
      }
    }
   ```

## 트러블 슈팅

- 인터넷에서 WebGL을 사용할 경우 인터넷 IME가 한글을 지원하지 않는다.
  한글 Input이 가능해지게 Scripts Component를 추가해야 함.
  <https://github.com/kou-yeung/WebGLInput> 에서 지원을 해줌.
  1. WebGLSupport.unitypackage 다운로드
  2. import하고 싶은 프로젝트를 열고 다운받은 파일 열기
  3. import 후, inputField 계열 GameObject에 Component WebGLInput 추가
  
  - (22.03.15 버전 기준 오류 발생) 수정하기
  1. 빌드 후, framework.js 파일 열기
  2. allocate(intArrayFromString(input.value), "i8", ALLOC_NORMAL);를
  allocate(intArrayFromString(input.value), ALLOC_NORMAL);로 변경
