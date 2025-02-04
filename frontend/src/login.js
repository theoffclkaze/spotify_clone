import React, { useState } from "react";
import axios from "axios";

const Login = () => {
    const [token, setToken] = useState("");

    const handleLogin = () => {
        axios.post("http://127.0.0.1:5000/login", {
            username: "kaZe",
            password: "admin"
        })
            .then(res => {
                if (res && res.data) {
                    setToken(res.data.access_token);
                } else {
                    console.log("Response is undefined or does not contain data");
                }
            })
            .catch(err => console.log(err.response ? err.response.data : err.message));
    };

    return (
        <div>
            <button onClick={handleLogin}>Login</button>
            {token && <p>Token: {token}</p>}
        </div>
    );
};

export default Login;