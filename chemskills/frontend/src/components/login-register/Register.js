import React, { useState } from 'react';

const Register = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const [first_name, setFirstName] = useState('');
    const [last_name, setLastName] = useState('');
    const [is_teacher, setIsTeacher] = useState(false);


    const handleUsernameChange = (e) => {
        setUsername(e.target.value);
    };

    const handlePasswordChange = (e) => {
        setPassword(e.target.value);
    };

    const handleEmailChange = (e) => {
        setEmail(e.target.value);
    };

    const handleFirstNameChange = (e) => {
        setFirstName(e.target.value);
    };

    const handleLastNameChange = (e) => {
        setLastName(e.target.value);
    };

    const handleIsTeacherChange = (e) => {
        setIsTeacher(e.target.value);
    };


    const handleSubmit = (e) => {
        e.preventDefault();
        // Check if username is already taken
        fetch(`http://localhost:8000/api/user?format=json&username=${username}`)
            .then(response => response.json())
            .then(data => {
                if (data.length > 0) {
                    alert('Username is already taken');
                } else {
                    // Continue with the registration process
                }
            })
            .catch(error => console.error('Error:', error));
        

    };

    return (
        <div>
            <h2>Register</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="username">Username:</label>
                    <input
                        type="text"
                        id="username"
                        value={username}
                        onChange={handleUsernameChange}
                    />
                </div>
                <div>
                    <label htmlFor="password">Password:</label>
                    <input
                        type="password"
                        id="password"
                        value={password}
                        onChange={handlePasswordChange} />
                </div>
                <div>
                    <label htmlFor="email">Email:</label>
                    <input
                        type="email"
                        id="email"
                        value={email}
                        onChange={handleEmailChange} />
                </div>
                <div>
                    <label htmlFor="first_name">First Name:</label>
                    <input
                        type="text"
                        id="first_name"
                        value={first_name}
                        onChange={handleFirstNameChange} />
                    <div>
                        <label htmlFor="last_name">Last Name:</label>
                        <input
                            type="text"
                            id="last_name"
                            value={last_name}
                            onChange={handleLastNameChange}
                        />
                    </div>
                    <div>
                        <label htmlFor="is_teacher">Are you a Teacher?</label>
                        <input
                            type="checkbox"
                            id="is_teacher"
                            value={is_teacher}
                            onChange={handleIsTeacherChange}
                        />
                    </div>
                </div>
                <button type="submit">Register</button>
            </form>
        </div>
    );
};

export default Register;