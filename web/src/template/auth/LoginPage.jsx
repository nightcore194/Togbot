import React, { useState } from 'react';
import axios from 'axios';

export default function Login(){
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/auth/login', {
                email,
                password,
            });
            setMessage(response.data.message);
            // Redirect or perform any additional actions on successful login
        } catch (error) {
            setMessage(error.response ? error.response.data.message : 'Login failed');
        }
    };

    return (
        <div>
            <h1>Login</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="username">Email:</label>
                <input type="email" name="username" value={username} onChange={(e) => setUsername(e.target.value)} required/>
                <br />
                <label htmlFor="password">Password:</label>
                <input type="password" name="password" value={password} onChange={(e) => setPassword(e.target.value)} required/>
                <br />
                <button type="submit">Login</button>
            </form>
            {message && (
                <ul>
                    <li>{message}</li>
                </ul>
            )}
        </div>
    );
}
