/* global localStorage */

import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles.css';

function LoginPage () {
  const [formData, setFormData] = useState({ username: '', password: '' });
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setError(null);

    fetch('/api/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    })
      .then(response => response.json())
      .then(data => {
        if (data.access) {
          localStorage.setItem('accessToken', data.access);
          navigate('/profile');
        } else if (data.error) {
          setError('Invalid credentials');
        }
      })
      .catch(error => {
        console.error('Error:', error);
        setError('An unexpected error occured');
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Login</h2>
      {error && <p className='error'>{error}</p>}
      <input
        type='text'
        name='username'
        placeholder='Username'
        value={formData.username}
        onChange={handleChange}
        required
      />
      <input
        type='password'
        name='password'
        placeholder='Password'
        value={formData.password}
        onChange={handleChange}
        required
      />
      <button type='submit'>Login</button>
    </form>
  );
}

export default LoginPage;
