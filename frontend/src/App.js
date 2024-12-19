import './App.css';
import Signin from './components/Signin.js';
import Welcome from './components/Welcome.js';
import { useState } from 'react';

function App() {
  const [loginFlag, setLoginFlag] = useState(false);
  return (
    loginFlag === false ?
      <div className="App"><Signin loginFlag={setLoginFlag} /></div>
      : <div className="App"><Welcome loginFlag={setLoginFlag} /></div>
  );
}

export default App;