import React, { Component } from "react";


export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <a href='/classroom-join'>Join a Classroom</a>
        <a href='/classroom-create'>Create a Classroom</a>
      </div>
    );
  }
}
