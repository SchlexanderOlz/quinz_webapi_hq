function LogoutForm({ authToken, setAuthToken  }) {
  const handleSubmit = async (e) => {
    e.preventDefault()
    const response = await fetch('http://127.0.0.1:5000/api/logout', {
      method: 'POST',
      headers: { 
        'Content-Type': 'application/json',
        'X-Auth-Token': authToken
      }
    })
    const data = await response.json()
    console.log(data)
    setAuthToken(null)
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Logout</h2>
      <button type="submit">Logout</button>
    </form>
  )
}

export default LogoutForm