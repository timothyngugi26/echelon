import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles.css';

function SignupPage () {
  const [formData, setFormData] = useState({ username: '', email: '', password: '' });
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);
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

    fetch('http://127.0.0.1:8000/api/signup/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    })
      .then(response => response.json())
      .then(data => {
        if (data.message) {
          setSuccess(data.message);
          setTimeout(() => {
            navigate('/login');
          }, 200);
        } else if (data.error) {
          setError(data.error);
        }
      })
      .catch(error => {
        console.error('Error:', error);
        setError('An unexpected error occured');
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Sign Up</h2>
      {error && <p className='error'>{error}</p>}
      {success && <p className='success'>{success}</p>}

      <input
        type='text'
        name='username'
        placeholder='Username'
        value={formData.username}
        onChange={handleChange}
        required
      />
      <input
        type='email'
        name='email'
        placeholder='Email'
        value={formData.email}
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
      <button type='submit'>Sign Up</button>
    </form>
  );
}
export default SignupPage;
