import React, { useState } from 'react';
import axios from 'axios';

export default function Login(){
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [display_name, setDisplay_name] = useState('');
    const [birthday, setBirthday] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/auth/signup', {
                username,
                email,
                display_name,
                birthday,
                password,
            });
            setMessage(response.data.message);
            // Redirect or perform any additional actions on successful login
        } catch (error) {
            setMessage(error.response ? error.response.data.message : 'User is already exist!');
        }
    };

    return (
        <div>
            <h1>Sign up</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="email">Email:</label>
                <input type="email" name="email" value={email} onChange={(e) => setEmail(e.target.value)}
                       required/>
                <br/>
                <label htmlFor="username">Username:</label>
                <input type="text" name="username" value={username} onChange={(e) => setUsername(e.target.value)}
                       required/>
                <br/>
                <label htmlFor="display_name">Display name:</label>
                <input type="text" name="display_name" value={display_name}
                       onChange={(e) => setDisplay_name(e.target.value)}/>
                <br/>
                <label htmlFor="birthday">Birthday:</label>
                <input type="date" name="birthday" value={birthday}
                       onChange={(e) => setBirthday(e.target.value)}/>
                <br/>
                <label htmlFor="password">Password:</label>
                <input type="password" name="password" value={password} onChange={(e) => setPassword(e.target.value)}
                       required/>
                <br/>
                <button type="submit">Sign up</button>
            </form>
            {message && (
                <ul>
                    <li>{message}</li>
                </ul>
            )}
        </div>
    );
};