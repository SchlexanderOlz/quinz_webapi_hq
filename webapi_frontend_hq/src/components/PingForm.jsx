import React, { useState } from 'react';

function PingForm({ authToken }) {
  const [pingResponse, setPingResponse] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const response = await fetch('http://127.0.0.1:5000/api/ping', {
      method: 'POST',
      headers: { 
        'Content-Type': 'application/json',
        'X-Auth-Token': authToken
      }
    });
    const data = await response.json();
    setPingResponse(data[0].result);
    console.log(data);
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Ping</h2>
      <button type="submit">Ping</button>
      {pingResponse && <div>Ping Response: {JSON.stringify(pingResponse)}</div>}
    </form>
  )
}

export default PingForm