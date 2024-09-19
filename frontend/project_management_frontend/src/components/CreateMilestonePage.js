import React, { useState } from 'react';
import '../styles.css';

function CreateMilestonePage () {
  const [milestoneName, setMilestoneName] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
  };

  return (
    <div className='create-milestone'>
      <h2>Create a New Milestone</h2>
      <form onSubmit={handleSubmit}>
        <input
          type='text'
          name='milestoneName'
          placeholder='Milestone Name'
          value={milestoneName}
          onChange={(e) => setMilestoneName(e.target.value)}
          required
        />
        <button type='submit'>Create Milestone</button>
      </form>
    </div>
  );
}

export default CreateMilestonePage;
