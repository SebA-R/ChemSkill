import React, { Component } from "react";

export default class ChemistryDashboard extends Component {
  constructor(props) {
    super(props);
    this.state = {
      userName: "John Doe", // Replace with the user's name fetched from your backend
      currentChapter: "Introduction to Chemistry", // Update dynamically based on the user's progress
      resources: [
        {
          title: "Chemical Reactions",
          // link: "https://example.com/chemical-reactions"
        },
        {
          title: "Periodic Table",
          link: "https://example.com/periodic-table"
        },
        // Add more resources as needed
      ]
    };
  }

  render() {
    const { userName, currentChapter, resources } = this.state;

    return (
      <div>
        {/* Navigation Bar */}
        <nav>
          <ul>
            <li>Dashboard</li>
            <li>Profile</li>
            <li>Settings</li>
            {/* Add more navigation items as needed */}
          </ul>
        </nav>

        {/* Dashboard Content */}
        <div>
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
      </div>
    );
  }
}
