import React, { useState, useEffect } from 'react';

function TaskProgress ({ projectId }) {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    fetch('/api/projects/${projectId}/')
      .then(response => response.json())
      .then(data => {
        const allTasks = data.milestones.flatMap(milestone => milestone.tasks);
        setTasks(allTasks);
      })
      .catch(error => console.error('Error fetching tasks:', error));
  }, [projectId]);

  const toDoCount = tasks.filter(task => task.status === 'to-do').length;
  const inProgressCount = tasks.filter(task => task.status === 'in-progress').length;
  const completedCount = tasks.filter(task => task.status === 'completed').length;

  return (
    <div className='task-progress'>
      <h2>Project Progress</h2>
      <p>To-Do: {toDoCount}</p>
      <p>In Progress: {inProgressCount}</p>
      <p>Completed: {completedCount}</p>
    </div>
  );
}

export default TaskProgress;
