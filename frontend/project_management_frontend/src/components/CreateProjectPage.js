import React, { useState } from 'react';
import '../styles.css';

function CreateProjectPage() {
  const [projectName, setProjectName] = useState('');

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
     .then((response) => response.json())
     .then((data) => {
       console.log("Project created successfully", data);
     })
     .catch((error) => {
       console.error("Error creating project:", error);
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
    </div>
  );
}

export default CreateProjectPage;
