import logo from './logo.svg';
import React from 'react';
import { HashRouter as Router, Routes, Route } from 'react-router-dom';
import ProfilePage from './components/ProfilePage';
import GetStartedPage from './components/GetStartedPage';
import IndexPage from './components/IndexPage';
import SignupPage from './components/SignupPage';
import LoginPage from './components/LoginPage';
import NotFoundPage from './components/NotFoundPage';
import './App.css';

function App() {
	console.log("App component Mounted");

  return (
    <Router>
      <Routes>
	  <Route exact path="/" element={<IndexPage />} />
	  <Route path="/profile" element={<ProfilePage />} />
          <Route path="/signup" element={<SignupPage />} />
          <Route path="/login" element={<LoginPage />} />
	  <Route path='/get-started' element={<GetStartedPage />} />
          <Route path="*" element={<NotFoundPage />} /> {/* 404 route */}
     </Routes>
   </Router>
  );
}

export default App;
