import React, { useState, useEffect } from 'react';

function MilestoneList ({ projectId }) {
  const [milestones, setMilestones] = useState([]);

  useEffect(() => {
    fetch('api/projects/${projectId}/milestone/')
      .then(response => response.json())
      .then(data => setMilestones(data))
      .catch(error => console.error('Error fetching milestones:', error));
  }, [projectId]);

  return (
    <div className='milestone-list'>
      <h2>Milestones</h2>
      <ul>
        {milestones.map(milestone => (
          <li key={milestone.id}>{milestone.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default MilestoneList;
