import { useState } from 'react';

function ToggleMotor({ authToken }) {
  const [isOn, setIsOn] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const endpoint = isOn ? 'turn_off' : 'turn_on';
    const response = await fetch(`http://127.0.0.1:5000/api/${endpoint}`, {
      method: 'POST',
      headers: { 
        'X-Auth-Token': authToken
      }
    });
    const data = await response.json();
    console.log(data);
    setIsOn(!isOn);
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Turn Motor {isOn ? 'Off' : 'On'}:</h2>
      <button type="submit">Turn {isOn ? 'Off' : 'On'}</button>
    </form>
  );
}

export default ToggleMotor;