import React, { useState, useEffect } from 'react';

const ClassRoomJoin = () => {
  const [userName, setUserName] = useState('John Doe');

  useEffect(() => {
    fetch('http://localhost:8000/api/user')  // Replace with your API endpoint
      .then(response => response.json())
      .then(data => {
        setUserName(data.userName);
      })
      .catch(error => console.error('Error:', error));
  }, []);

  return (
  <div>
  {/* Navigation Bar */ }
  <nav>
    <ul>
      <li>Dashboard</li>
      <li>Profile</li>
      <li>Settings</li>
      {/* Add more navigation items as needed */}
    </ul>
  </nav>

  {/* Dashboard Content */ }
    <h1>Welcome, {userName}!</h1>
    <p>You are currently studying: {currentChapter}</p>

    <h2>Resources:</h2>
    <ul>
      {resources.map((resource, index) => (
        <li key={index}>
          <a href={resource.link} target="_blank" rel="noopener noreferrer">
            {resource.title}
          </a>
        </li>
      ))}
    </ul>
      </div>
    );

};

export default ClassRoomJoin;