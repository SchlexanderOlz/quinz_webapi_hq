import { useState } from 'react'

function BrowseForm({ authToken }) {
  const [varPath, setVarPath] = useState('')
  const [mode, setMode] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    const response = await fetch('http://127.0.0.1:5000/api/browse', {
      method: 'POST',
      headers: { 
        'Content-Type': 'application/json',
        'X-Auth-Token': authToken
      },
      body: JSON.stringify({ var: varPath, mode })
    })
    const data = await response.json()
    console.log(data)
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Browse</h2>
      <label>
        Variable Path:
        <input type="text" value={varPath} onChange={(e) => setVarPath(e.target.value)} />
      </label>
      <label>
        Mode:
        <input type="text" value={mode} onChange={(e) => setMode(e.target.value)} />
      </label>
      <button type="submit">Browse</button>
    </form>
  )
}

export default BrowseForm