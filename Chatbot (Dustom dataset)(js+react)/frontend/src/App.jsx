import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Chat from './Pages/Chat.jsx';


function App() {
  return (
    <Router>
      <div>
        <header>
          <Routes>
            <Route path="/" element={<Chat />} />
          </Routes>
        </header>
      </div>
    </Router>
  );
}

export default App;
