import React from "react";
import { useNavigate } from "react-router-dom";

const Home = () => {
  const navigate = useNavigate();

  const cardStyle = {
    background: "#1e293b",
    padding: "25px",
    borderRadius: "15px",
    cursor: "pointer",
    textAlign: "center",
    fontSize: "18px",
    fontWeight: "600",
    transition: "0.3s",
    width: "220px"
  };

  return (
    <div style={{
      minHeight: "100vh",
      background: "#0f172a",
      color: "white",
      textAlign: "center",
      padding: "40px"
    }}>
      <h1 style={{ marginBottom: "40px" }}>🏋️ AI Gym Assistant</h1>

      <div style={{
        display: "grid",
        gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))",
        gap: "25px",
        justifyItems: "center"
      }}>
        <div style={cardStyle} onClick={() => navigate("/trainer")}>
          🎯 AI Trainer
        </div>

        <div style={cardStyle} onClick={() => navigate("/diet")}>
          🥗 Diet Planner
        </div>

        <div style={cardStyle} onClick={() => navigate("/chat")}>
          🤖 Gym Buddy
        </div>
        <div style={cardStyle} onClick={() => navigate("/analytics")}>
         📊 Analytics
        </div>

        <div style={cardStyle} onClick={() => navigate("/habit")}>
          📊 Habit Tracker
        </div>
      </div>
    </div>
  );
};

export default Home;