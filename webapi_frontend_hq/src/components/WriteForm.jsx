import { useState } from 'react'

function WriteForm({ authToken }) {
  const [varPath, setVarPath] = useState('')
  const [value, setValue] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    const response = await fetch('http://127.0.0.1:5000/api/write', {
      method: 'POST',
      headers: { 
        'Content-Type': 'application/json',
        'X-Auth-Token': authToken
      },
      body: JSON.stringify({ var: varPath, value })
    })
    const data = await response.json()
    console.log(data)
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Write</h2>
      <label>
        Variable Path:
        <input type="text" value={varPath} onChange={(e) => setVarPath(e.target.value)} />
      </label>
      <label>
        Value:
        <input type="text" value={value} onChange={(e) => setValue(e.target.value)} />
      </label>
      <button type="submit">Write</button>
    </form>
  )
}

export default WriteForm