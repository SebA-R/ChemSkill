import React, { Component } from "react";

export default class ClassRoomJoin extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>
                <h2>Enter a Class Code:</h2>
                <form>
                    <div>
                        <label htmlFor="class_code">Class Code:</label>
                        <input
                            type="text"
                            id="class_code"
                        />
                    </div>
                    <button type="submit">Join Class</button>
                </form>
            </div>
        );
    }
}