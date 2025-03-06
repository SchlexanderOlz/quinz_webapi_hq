import { useState } from 'react'
import './App.css'
import LoginForm from './components/LoginForm'
import PermissionsForm from './components/PermissionsForm'
import BrowseForm from './components/BrowseForm'
import ReadForm from './components/ReadForm'
import WriteForm from './components/WriteForm'
import PingForm from './components/PingForm'
import LogoutForm from './components/LogoutForm'
import WriteSpeedForm from './components/WriteSpeedForm'
import ToggleMotor from './components/ToggleMotor'

function App() {
  const [authToken, setAuthToken] = useState(null)

  return (
    <div className="App">
      <h1>API Endpoints</h1>
      <LoginForm setAuthToken={setAuthToken} />
      <ToggleMotor authToken={authToken} />
      <PermissionsForm authToken={authToken} />
      <WriteForm authToken={authToken} />
      <PingForm authToken={authToken} />
      <LogoutForm authToken={authToken} setAuthToken={setAuthToken} />
      <WriteSpeedForm authToken={authToken} />
    </div>
  )
}

export default App