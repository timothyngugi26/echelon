import React, { useState, useEffect } from 'react';
import '../styles.css';


function ProjectList() {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, SetError] = useState(null);

  useEffect(() => {
    fetch('/api/projects/')
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to fetch projects');
        }
        return response.json();
       })
       .then(data => {
         setProjects(data);
         setLoading(false);
       })
       .catch(error => {
         setError(error.message);
         setLoading(false);
       });
   }, []);

   if (loading) {
      return <div className='loading'>Loading Projects...</div>;
   }

   if (error) {
      return <div className='error-message'>Error: {error}</div>;
   }

  return (
    <div classname='project-list-container'>
      <h2>Projects</h2>
      <ul className='project-list'>
        {projects.length > 0 ? (
          projects.map(project => (
           <li key={project.id} className='project-item'>
             {project.name}
           </li>
        ))
      ) : (
        <li>No projects found</li>
       )}
      </ul>
    </div>
  );
}

export default ProjectList;
