import React, { useState, useEffect } from 'react';
import '../styles.css';

function ProjectProgressPage () {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/projects/')
      .then(response => response.json())
      .then(data => {
        setProjects(data.projects);
        setLoading(false);
      })

      .catch(error => {
        console.error('Error fetching projects:', error);
        setError('An error occured while fetching project data');
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }
  if (error) {
    return <p className='error'>{error}</p>;
  }

  return (
    <div clasName='project-progress'>
      <h2>Project Progress</h2>
      {projects.length === 0
        ? (
          <p>No projects available.</p>
          )
        : (
          <div className='projects-list'>
            {projects.map(project => (
              <div key={project.id} className='project'>
                <h3>{project.name}</h3>
                <p>Status: {project.status}</p>
                <p>Progress: {project.progress}%</p>
                <div className='milestones'>
                  <h4>Milestones:</h4>
                  {project.milestones.map(milestone => (
                    <div key={milestone.id} className='milestone'>
                      <p>{milestone.name}- {milestone.status} ({milestone.progress}%)</p>
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
          )}
    </div>
  );
}

export default ProjectProgressPage;
