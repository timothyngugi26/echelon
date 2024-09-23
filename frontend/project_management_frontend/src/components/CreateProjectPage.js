import React, { useState } from 'react';
import '../styles.css';

function CreateProjectPage() {
  const [projectName, setProjectName] = useState('');
  const [message, setMessage] = useState(null);

  const handleSubmit = (event) => {
      event.preventDefault();
      const projectData = {
	  name: projectName,
  };

  fetch("/api/projects/", {
     method: "POST",
     headers: {
       "Content-Type": "application/json",
     },
     body: JSON.stringify(projectData),
   })
     .then((response) => {
        setMessage("Project created successfully!");
        setProjectName('');
     })
     .catch((error) => {
       setMessage("Error creating project. Please try again.");
     });
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
      {message && <div className="message">{message}</div>}
    </div>
  );
}

export default CreateProjectPage;
