import React from 'react';
import RegisterForm from './components/RegisterForm';
import LoginForm from './components/LoginForm';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Super Agent - Gestión Estudiantil</h1>
        <LoginForm />
        <RegisterForm />
      </header>
    </div>
  );
}

export default App;