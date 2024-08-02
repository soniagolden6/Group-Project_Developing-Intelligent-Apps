// JavaScript Frontend

import React, { useState } from 'react';

function App() {
  const [input, setInput] = useState('');
  const [prediction, setPrediction] = useState(null);

  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  const handlePredict = async () => {
    const response = await fetch('/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ review: input }),
    });
    const result = await response.json();
    setPrediction(result.sentiment);
  };

  return (
    <div>
      <h1>Sentiment Analysis App</h1>
      <input type="text" value={input} onChange={handleInputChange} />
      <button onClick={handlePredict}>Predict</button>
      {prediction && <div>Prediction: {prediction}</div>}
    </div>
  );
}

export default App;
