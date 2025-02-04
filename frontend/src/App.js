import React, { useEffect, useState } from "react";
import axios from "axios";
import Login from "./login";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/ping").then((response) => {
      setMessage(response.data.message);
    });
  }, []);

  return (
      <div>
        <h1>{message}</h1>
        <Login />
      </div>
  );
}

export default App;