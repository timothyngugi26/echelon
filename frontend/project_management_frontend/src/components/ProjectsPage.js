import React, { useState, useEffect } from 'react';
import '../ProjectsPage.css';


function ProjectsPage () {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('/api/projects/')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        setProjects(data);
        setLoading(false);
      })
      .catch(error => {
        setError(error);
        setLoading(false);
      });
  }, []);
  if (loading) {
    return <div className="loading-spinner">Loading...</div>;
  }

  if (error) {
    return <div className="error-message">Error: {error.message}</div>;
  }

  return (
    <div className="projects-container">
      <h1 className="projects-title">Projects</h1>
      {projects.length === 0? (
        <p className="no-proojects">No projects Available. Start by creating a new   one!</p>
       ) : (
      <ul className="projects-list">
        {projects.map(project => (
          <li key={project.id} className="project-item">
             <h2>{project.name}</h2>
             <p>{project.description}</p>
          </li>
        ))}
      </ul>
     )}
    </div>
  );
}

export default ProjectsPage;
