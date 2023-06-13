import { useState, useEffect } from "react";
import Button from "./Button";
import styles from "./App.module.css";

function App() {
  const [counter, setValue] = useState(0);  // value, modifier, default = 0
  const [keyword, setKeyword] = useState("");
  const onClick = () => setValue((prev) => prev + 1);
  const onChange = (event) => setKeyword(event.target.value);
  const iRunOnlyOnce = () => {console.log("한번만 작동함! API 실행 등에 유용!")};

  console.log("render 할때마다 작동함!");
  useEffect(iRunOnlyOnce, []);  // 두번째 argument가 비어있으니 한 번 만 실행됨
  useEffect(() => {
    if (keyword !== "") {  // 최초 rendering때 실행하는 것을 막으려고
      console.log("검색 중 : ", keyword)
    }    
  }, [keyword]); // keyword가 변할 때만 실행됨
  useEffect(() => {console.log("카운터 변할때만 실행됨!")}, [counter])
  useEffect(() => {console.log("카운터, 검색어 둘 중 하나만 변해도 실행됨!")}, [counter, keyword])
  
  return (
    <div>
      <h1 className={styles.title}>Welcome back!</h1>
      <input 
        type="text" 
        placeholder="검색 bar" 
        value={keyword}
        onChange={onChange}></input>
      <h2>{counter}</h2>
      <Button text={"props!"}/>
      <button onClick={onClick}>카운터 증가</button>
    </div>
  );
}

export default App;
