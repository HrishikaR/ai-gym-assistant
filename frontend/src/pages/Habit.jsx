import React, { useState, useEffect } from "react";
import axios from "axios";

const Habit = () => {
  const [day, setDay] = useState("");
  const [status, setStatus] = useState("done");
  const [history, setHistory] = useState([]);
  const [analysis, setAnalysis] = useState("");
  const [loading, setLoading] = useState(false);

  // 🔥 Load history on page load
  useEffect(() => {
    fetchHistory();
  }, []);

  const fetchHistory = async () => {
    try {
      const res = await axios.get("http://127.0.0.1:5000/habit/history");
      setHistory(res.data);
    } catch {
      console.log("Error fetching history");
    }
  };

  // 🔥 Add habit
  const addHabit = async () => {
    if (!day) return alert("Enter day");

    try {
      await axios.post("http://127.0.0.1:5000/habit/add", {
        day,
        status,
      });

      fetchHistory(); // refresh
      setDay("");
    } catch {
      alert("Error adding habit");
    }
  };

  // 🔥 Analyze
  const analyze = async () => {
    setLoading(true);

    try {
      const res = await axios.get("http://127.0.0.1:5000/habit/analyze");
      setAnalysis(res.data.result);
    } catch {
      setAnalysis("Error analyzing");
    }

    setLoading(false);
  };

  return (
    <div style={{
      minHeight: "100vh",
      background: "#0f172a",
      color: "white",
      padding: "30px"
    }}>
      <h1 style={{ textAlign: "center" }}>📊 Habit Tracker</h1>

      {/* 🔹 Add Habit */}
      <div className="card">
        <input
          placeholder="Enter Day (e.g. Monday)"
          value={day}
          onChange={(e) => setDay(e.target.value)}
        />

        <select onChange={(e) => setStatus(e.target.value)}>
          <option value="done">Done</option>
          <option value="missed">Missed</option>
        </select>

        <button onClick={addHabit}>Add Habit</button>
      </div>

      {/* 🔹 History */}
      <div className="card">
        <h3>📅 History</h3>

        {history.length === 0 ? (
          <p>No data yet</p>
        ) : (
          history.map((h, i) => (
            <p key={i}>
              {h.day} — {h.status}
            </p>
          ))
        )}
      </div>

      {/* 🔹 Analyze */}
      <div className="card">
        <button onClick={analyze}>
          {loading ? "Analyzing..." : "Analyze Habits"}
        </button>

        <div style={{ whiteSpace: "pre-wrap", marginTop: "15px" }}>
          {analysis}
        </div>
      </div>
    </div>
  );
};

export default Habit;