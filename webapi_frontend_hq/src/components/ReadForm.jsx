import { useState } from 'react'

function ReadForm({ authToken }) {
  const [varPath, setVarPath] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    const response = await fetch('http://127.0.0.1:5000/api/read', {
      method: 'POST',
      headers: { 
        'Content-Type': 'application/json',
        'X-Auth-Token': authToken
      },
      body: JSON.stringify({ var: varPath })
    })
    const data = await response.json()
    console.log(data)
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Read</h2>
      <label>
        Variable Path:
        <input type="text" value={varPath} onChange={(e) => setVarPath(e.target.value)} />
      </label>
      <button type="submit">Read</button>
    </form>
  )
}

export default ReadForm