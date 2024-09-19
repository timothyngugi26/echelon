import React, { useState } from 'react';
import '../styles.css';

function CreateProjectPage () {
  const [projectName, setProjectName] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
  };

  return (
    <div className='create-project'>
      <h2>Create a New Project</h2>
      <form onSubmit={handleSubmit}>
        <input
          type='text'
          name='projectName'
          placeholder='Project Name'
          value={projectName}
          onChange={(e) => setProjectName(e.target.value)}
          required
        />
        <button type='submit'>Create Project</button>
      </form>
    </div>
  );
}

export default CreateProjectPage;
