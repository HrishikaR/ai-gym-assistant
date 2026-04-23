import React, { useEffect, useState } from "react";
import axios from "axios";
import {
  Chart as ChartJS,
  BarElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend,
} from "chart.js";
import { Bar } from "react-chartjs-2";

ChartJS.register(CategoryScale, LinearScale, BarElement, Tooltip, Legend);

const Analytics = () => {
  const [data, setData] = useState([]);
  const [stats, setStats] = useState({
    total: 0,
    done: 0,
    missed: 0,
    consistency: 0,
  });

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    const res = await axios.get("http://127.0.0.1:5000/habit/history");
    const habits = res.data;

    let done = habits.filter((h) => h.status === "done").length;
    let missed = habits.length - done;
    let total = habits.length;
    let consistency = total ? (done / total) * 100 : 0;

    setStats({ total, done, missed, consistency });
    setData(habits);
  };

  const chartData = {
    labels: ["Done", "Missed"],
    datasets: [
      {
        label: "Habit Stats",
        data: [stats.done, stats.missed],
        backgroundColor: ["#22c55e", "#ef4444"],
      },
    ],
  };

  return (
    <div style={{
      minHeight: "100vh",
      background: "#0f172a",
      color: "white",
      padding: "30px"
    }}>
      <h1 style={{ textAlign: "center", marginBottom: "30px" }}>
        📊 Admin Dashboard
      </h1>

      {/* 🔥 TOP STATS */}
      <div style={{
        display: "grid",
        gridTemplateColumns: "repeat(auto-fit, minmax(200px,1fr))",
        gap: "20px"
      }}>
        <div className="card">📅 Total Days<br /><b>{stats.total}</b></div>
        <div className="card">✅ Done<br /><b>{stats.done}</b></div>
        <div className="card">❌ Missed<br /><b>{stats.missed}</b></div>
        <div className="card">📈 Consistency<br /><b>{stats.consistency.toFixed(1)}%</b></div>
      </div>

      {/* 🔥 CHART */}
      <div className="card" style={{ marginTop: "30px" }}>
        <h3>📊 Performance Overview</h3>
        <Bar data={chartData} />
      </div>

      {/* 🔥 LOWER SECTION */}
      <div style={{
        display: "grid",
        gridTemplateColumns: "1fr 1fr",
        gap: "20px",
        marginTop: "30px"
      }}>

        {/* RECENT ACTIVITY */}
        <div className="card">
          <h3>📌 Recent Activity</h3>
          {data.slice(-5).map((h, i) => (
            <p key={i}>
              {h.day} — {h.status === "done" ? "✅ Done" : "❌ Missed"}
            </p>
          ))}
        </div>

        {/* SYSTEM STATUS */}
        <div className="card">
          <h3>⚙️ System Status</h3>
          <p>✔ AI Models: Active</p>
          <p>✔ Database: Connected</p>
          <p>✔ APIs: Running</p>
          <p>✔ Modules: 4 Active</p>
        </div>

      </div>
    </div>
  );
};

export default Analytics;