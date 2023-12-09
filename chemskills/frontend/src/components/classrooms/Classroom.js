import React, { useState, useEffect } from 'react';

const ClassRoomJoin = () => {
  const [username, setUserName] = useState('John Doe');
  const [currentChapter, setCurrentChapter] = useState('Chapter 1');


  useEffect(() => {
    setUserName(sessionStorage.getItem('username'));
    setCurrentChapter(sessionStorage.getItem('currentChapter'));
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
    <h1>Welcome, {username}!</h1>
    <p>You are currently studying: {currentChapter}</p>

      </div>
    );

};

export default ClassRoomJoin;