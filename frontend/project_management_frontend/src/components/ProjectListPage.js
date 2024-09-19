import React, { useState, useEffect } from 'react';

function ProjectList () {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    fetch('/api/projects/')
      .then(response => response.json())
      .then(data => setProjects(data))
      .catch(error => console.error('Error fetching projects:', error));
  }, []);

  return (
    <div classname='project-list'>
      <h2>Projects</h2>
      <ul>
        {projects.map(project => (
          <li key={project.id}>{project.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default ProjectList;
