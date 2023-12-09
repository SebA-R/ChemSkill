import React, { Component } from "react";

export default class ClassRoomJoin extends Component {
  constructor(props) {
    super(props);
  }

  button() {
    return (
      <div>
        <button type="button" onClick={this.handleClick}>
          Join
        </button>
      </div>
      );
    }

  render() {
    return (
      <div>
        <p>This is not a Classroom page</p>
      </div>
    );
  }
}
