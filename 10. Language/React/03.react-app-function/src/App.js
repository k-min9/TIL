import { useState } from "react";
import Button from "./Button";
import styles from "./App.module.css";

function App() {
  const [counter, setValue] = useState(0);  // value, modifier, default = 0
  const onClick = () => setValue((prev) => prev + 1);

  return (
    <div>
      <h1 className={styles.title}>Welcome back!</h1>
      <h2>{counter}</h2>
      <Button text={"props!"}/>
      <button onClick={onClick}>카운터 증가</button>
    </div>
  );
}

export default App;
