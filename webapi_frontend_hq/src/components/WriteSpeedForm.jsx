import { useState } from 'react'

function WriteSpeedForm({ authToken }) {
  const [varPath, setVarPath] = useState('\"Motor\".Sollgeschwindigkeit')
  const [value, setValue] = useState()

  const handleSubmit = async (e) => {
    e.preventDefault()
    const response = await fetch('http://127.0.0.1:5000/api/write_speed', {
      method: 'POST',
      headers: { 
        'Content-Type': 'application/json',
        'X-Auth-Token': authToken
      },
      body: JSON.stringify({ var: varPath, value: Number(value) })
    })
    const data = await response.json()
    console.log(data)
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Write Speed</h2>
      <label>
        Value:
        <input type="number" value={value} onChange={(e) => setValue(Number(e.target.value))} />
      </label>
      <button type="submit">Write Speed</button>
    </form>
  )
}

export default WriteSpeedForm