import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [title, setTitle] = useState<string>('not clicked');
  const [count, setCount] = useState<number>(0);

  const handleLinkClick = () => {
    setTitle("clicked");
  }

  const handleUpClick = () => {
    setCount((count) => count + 1);
  }

  const handleDownClick = () => {
    if (count > 0) {
      setCount((count) => count - 1);
    }
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
          onClick={handleLinkClick}
        >
          Learn React {title}
        </a>

        <p>Count is {count}</p>
        <button onClick={handleUpClick}>up</button>
        <button onClick={handleDownClick}>down</button>
      </header>
    </div>
  );
}

export default App;
