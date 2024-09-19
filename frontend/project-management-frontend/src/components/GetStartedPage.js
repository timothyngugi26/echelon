import React from 'react';
import { Link } from 'react-router-dom';
import '../styles.css';

function GetStartedPage () {
  return (
    <div className='get-started'>
      <h2>Welcome to Echelon</h2>
      <p>Get Started with your Project</p>

      <div className='features'>
        <div className='feature'>
          <h3>Create a Project</h3>
          <Link to='/create-project'><button>Create Project</button></Link>
        </div>

        <div className='feature'>
          <h3>Create Milestones</h3>
          <p>Organize project into milestones</p>
          <Link to='/create-milestone'><button>Create Milestones</button></Link>
        </div>

        <div className='feature'>
          <h3>Create Tasks</h3>
          <p>Add tasks to milestones.</p>
          <Link to='/create-task'><button>Create Task</button></Link>
        </div>

        <div className='feature'>
          <h3>Project Progress</h3>
          <p>Monitor overall progress of your projects.</p>
          <Link to='/project-progress'><button>Project Progress</button></Link>
        </div>
      </div>
    </div>
  );
}

export default GetStartedPage;
