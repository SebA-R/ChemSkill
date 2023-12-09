import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";
import ClassroomJoin from "./classrooms/ClassroomJoinPage";
import Classroom from "./classrooms/Classroom";
import Login from "./login-register/Login";
import Register from "./login-register/Register";
import {
    BrowserRouter,
    Routes,
    Route,
    Link,
} from "react-router-dom";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<HomePage/>} />
          <Route path="/classroom-join" element={<ClassroomJoin/>} />
          <Route path="/classroom" element={<Classroom />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
        </Routes>
      </BrowserRouter>
    );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);
