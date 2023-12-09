import React, { useState } from 'react';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleUsernameChange = (e) => {
    setUsername(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch(`${window.location.origin}/api/user?format=json&username=${username}&password=${password}`)
      .then(response => response.json())
      .then(data => {
        if (data.length > 0) {
          alert('Username is already taken');
        } else if (8 > password.length || password.length > 20 ) {
          alert('Password must be between 8 and 20 characters');          
        } else {
          // Continue with the registration process
          fetch(`${window.location.origin}/api/user`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username: username, password: password }),
          })
            .then(response => response.json())
            .then(data => {
              console.log('Success:', data);
              sessionStorage.setItem('username', username);
              window.location.href = '/classroom-join';
            })
            .catch((error) => {
              console.error('Error:', error);
            });
        }
      })
      .catch(error => console.error('Error:', error));
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="username" className="form-label">Username:</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={handleUsernameChange}
            className="form-input"
          />
        </div>
        <div className="form-group">
          <label htmlFor="password" className="form-label">Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={handlePasswordChange}
            className="form-input"
          />
        </div>
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default Login;