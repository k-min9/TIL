import React, { useState, useEffect } from "react";
import Unity, { UnityContext } from "react-unity-webgl";

const unityContext = new UnityContext({
  loaderUrl: "build/01.Dodge.loader.js",
  dataUrl: "build/01.Dodge.data",
  frameworkUrl: "build/01.Dodge.framework.js",
  codeUrl: "build/01.Dodge.wasm",
});

function App() {
  const [speed, SetSpeed] = useState(0);

  useEffect(function() {
    unityContext.on("GetSpeed", function(speed) {
      SetSpeed(speed);
    });
  }, []);

  function speedIncrease() {
    // parameter : gameObjectName, methodName, parameter(string, number, boolean)
    unityContext.send("Player", "SpeedUp");
  }

  function speedDecrease() {
    unityContext.send("Player", "SpeedDown");
  }

  function handleOnClickFullscreen() {
    unityContext.setFullscreen(true);
  }

  return (
  <div>
    <div> 현재 속도 : {speed}</div>
    <button onClick={speedIncrease}>이동속도 증가</button>
    <button onClick={speedDecrease}>이동속도 감소</button>
    <button onClick={handleOnClickFullscreen}>Fullscreen</button>
    <div>
      <Unity style={{width:'1080px', height:'720px', border: "5px solid black", background: "grey"}} unityContext={unityContext} />
    </div>
  </div>
  );
}

export default App;
