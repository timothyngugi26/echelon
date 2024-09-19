import React from 'react';
import { Link } from 'react-router-dom';
// import './NotfoundPage.css';

const NotFoundPage = () => (
  <div className='not-found-container'>
    <h1>404 - Page Not Found</h1>
    <Link to='/'>Go back to Home</Link>
  </div>
);

export default NotFoundPage;
