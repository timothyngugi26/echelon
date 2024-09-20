import logo from './logo.svg';
import React from 'react';
import { HashRouter as Router, Routes, Route } from 'react-router-dom';
import ProfilePage from './components/ProfilePage';
import GetStartedPage from './components/GetStartedPage';
import IndexPage from './components/IndexPage';
import ProjectsPage from './components/ProjectsPage';
import SignupPage from './components/SignupPage';
import LoginPage from './components/LoginPage';
import CreateProjectPage from './components/CreateProjectPage';
import CreateMilestonePage from './components/CreateMilestonePage';
import CreateTaskPage from './components/CreateTaskPage';
import MilestoneListPage from './components/MilestoneListPage';
import ProgressPage from './components/ProgressPage';
import ProjectListPage from './components/ProjectListPage';
import TaskListPage from './components/TaskListPage';
import NotFoundPage from './components/NotFoundPage';
import TaskProgress from './components/TaskProgress';
import './App.css';

function App () {
  console.log('App component Mounted');

  return (
    <Router>
      <Routes>
        <Route exact path='/' element={<IndexPage />} />
        <Route exact path='/profile' element={<ProfilePage />} />
        <Route exact path='/signup' element={<SignupPage />} />
        <Route exact path='/login' element={<LoginPage />} />
        <Route exact path='/get-started' element={<GetStartedPage />} />
        <Route exact path='/projects' element={<ProjectsPage />} />
        <Route exact path='/create-project' element={<CreateProjectPage />} />
        <Route exact path='/create-milestone' element={<CreateMilestonePage />} />
		<Route exact path='/milestones' element={<MilestoneListPage />} />
		<Route exact path='progress' element={<ProgressPage />} />
        <Route exact path='/tasks' element={<TaskListPage />} />
        <Route exact path='/project-list' element={<ProjectListPage />} />
        <Route exact path='/create-task' element={<CreateTaskPage />} />
		<Route exact path='/task-progress' element={<TaskProgress />} />
        <Route path='*' element={<NotFoundPage />} /> {/* 404 route */}
      </Routes>
    </Router>
  );
}

export default App;
