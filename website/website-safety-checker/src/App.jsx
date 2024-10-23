import React from 'react';
import './App.css'; 
import Home_Pg from './components/Home_Pg';

function App() {
  return (
    <div className="app-container">
      {/* <header className="app-header">
        <h1>Website Safety Checker</h1>
        <p>Enter a website URL to find out if it is safe to visit!</p>
      </header> */}
      <main>
        <Home_Pg/>
      </main>
    </div>
  );
}

export default App;
