import React from 'react';
import { Link } from 'react-router-dom';
import '../styles.css';

function ProfilePage () {
  return (
    <div className='profile-container'>
      <div className='profile-header'>
        <img src='/build/static/Screenshot 2024-09-16 150014.png' alt='Profile' className='profile-pic' />
        <span className='username'>Username</span>
      </div>
      <div className='icon-container'>
        <Link to='/projects' className='icon'>Projects</Link>
        <Link to='/project-in-progress' className='icon'>Project in Progress</Link>
      </div>
    </div>
  );
}

export default ProfilePage;
