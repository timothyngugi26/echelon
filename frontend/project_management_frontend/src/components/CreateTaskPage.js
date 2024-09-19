import React, { useState } from 'react';
import '../styles.css';

function CreateTaskPage () {
  const [taskName, setTaskName] = useState('');
  const [milestone, setMilestone] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
  };

  return (
    <div className='create-task'>
      <h2>Create a New Task</h2>
      <form onSubmit={handleSubmit}>
        <input
          type='text'
          name='taskName'
          placeholder='Task Name'
          value={taskName}
          onChange={(e) => setTaskName(e.target.value)}
          required
        />

        <input
          type='text'
          name='milestone'
          placeholder='Milestone'
          value={milestone}
          onChange={(e) => setMilestone(e.target.value)}
          required
        />
        <button type='submit'>Create Task</button>
      </form>
    </div>
  );
}

export default CreateTaskPage;
