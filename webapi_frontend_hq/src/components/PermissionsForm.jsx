import React, { useState } from 'react';

function PermissionsForm({ authToken }) {
  const [permissions, setPermissions] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch('http://127.0.0.1:5000/api/permissions', {
      method: 'POST',
      headers: { 
        'Content-Type': 'application/json',
        'X-Auth-Token': authToken
      }
    });
    const data = await response.json();
    setPermissions(data[0].result);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <h2>Get Permissions</h2>
        <button type="submit">Get Permissions</button>
      </form>
      {permissions.length > 0 && (
        <div>
          <h3>Permissions:</h3>
          <ul>
            {permissions.map((permission, index) => (
              <li key={index}>{permission.name}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default PermissionsForm;