import React, { useState } from "react";
import axios from "axios";

const Chat = () => {
  const [msg, setMsg] = useState("");
  const [res, setRes] = useState("");
  const [loading, setLoading] = useState(false);

  const send = async () => {
    if (!msg) {
      alert("Enter a question");
      return;
    }

    setLoading(true);

    try {
      const r = await axios.post("http://127.0.0.1:5000/chat", {
        message: msg,
      });

      setRes(r.data.response);
    } catch (err) {
      console.error(err);
      setRes("Server error ❌");
    }

    setLoading(false);
  };

  return (
    <div style={{
      minHeight: "100vh",
      background: "#0f172a",
      color: "white",
      padding: "30px",
      textAlign: "center"
    }}>
      <h1>🤖 Gym Buddy</h1>

      <div className="card">
        <input
          value={msg}
          onChange={(e) => setMsg(e.target.value)}
          placeholder="Ask fitness question..."
        />

        <button onClick={send}>
          {loading ? "Thinking..." : "Send"}
        </button>
      </div>

      <div className="card" style={{ whiteSpace: "pre-wrap" }}>
        {res}
      </div>
    </div>
  );
};

export default Chat;