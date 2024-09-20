import React, { useState, useEffect } from 'react';


function ProjectsPage() {
   const [projects, setProjects] =useState([]);
   const [loading, setLoading] = useState(true);
   const [error, setError] = useState(null);

   useEffect(() => {
       fetch('/api/projects/')
        .then(response =>  {
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
        })
    }, []);
    if (loading) {
      return <div>Loading...</div>;
    }

    if (error) {
      return <div>Error: {error.message}</div>;
    }

    return (
      <div>
         <h1>Projects</h1>
         <ul>
            {projects.map(project => (
               <li key={project.id}>
                  {project.name} - {project.description}  
               </li>
            ))}
         </ul>
      </div>
    );
   }

   export default ProjectsPage;
