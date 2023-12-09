import React, { Component } from "react";


export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <a href='/find-mass'>Get quizzed</a>
        <a href='/find-mol'>Get quizzed on molar mass!</a>
        <a href='/find-lim-reag'>Get quizzed on limiting reagents!</a>
      </div>
    );
  }
}
