import React, { useState, useEffect } from 'react';

function TaskList ({ milestoneId }) {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    fetch('/api/milestones/${milestoneId}/tasks/')
      .then(response => response.json())
      .then(data => setTasks(data))
      .catch(error => console.error('Error fetching tasks:', error));
  }, [milestoneId]);

  return (
    <div className='task-list'>
      <h2>Tasks</h2>
      <ul>
        {tasks.map(task => (
          <li key={task.id}>{task.description} - {task.status}</li>
        ))}
      </ul>
    </div>
  );
}

export default TaskList;
