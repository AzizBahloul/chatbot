import React, { useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS

const Chat = () => {
  const [input, setInput] = useState('');
  const [response, setResponse] = useState('');

  const sendMessage = async () => {
    try {
      const res = await axios.post('http://localhost:5000/api/Chat', { message: input });
      setResponse(res.data.message);
    } catch (error) {
      console.error(error);
    }
  };

  const handleKeyDown = async (e) => {
    if (e.key === 'Enter') {
      await sendMessage();
    }
  };

  return (
    <div className="container">
      <h1>chtagpt 69</h1>
      <div className="card chat-box">
        <div className="card-body message-container">
          <p className="card-text">User: {input}</p>
          <p className="card-text">Bot: {response}</p>
        </div>
        <div className="card-footer input-container">
          <input
            type="text"
            className="form-control"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown} // Add event listener for "Enter" key
          />
          <button className="btn btn-primary" onClick={sendMessage}>Send</button>
        </div>
      </div>
    </div>
  );
};

export default Chat;
