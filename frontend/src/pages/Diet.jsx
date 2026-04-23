import React, { useState } from "react";
import axios from "axios";

const Diet = () => {
  const [data, setData] = useState({
    weight: "",
    height: "",
    age: "",
    goal: "loss"
  });

  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setData({ ...data, [e.target.name]: e.target.value });
  };

  const handleSubmit = async () => {
    setLoading(true);

    try {
      const res = await axios.post("http://127.0.0.1:5000/diet", data);
      setResult(res.data.result);
    } catch {
      setResult("Error fetching diet");
    }

    setLoading(false);
  };

  return (
    <div>
      <h1>🥗 Diet Planner</h1>

      <div className="card">
        <input name="weight" placeholder="Weight" onChange={handleChange} />
        <input name="height" placeholder="Height" onChange={handleChange} />
        <input name="age" placeholder="Age" onChange={handleChange} />

        <select name="goal" onChange={handleChange}>
          <option value="loss">Weight Loss</option>
          <option value="gain">Muscle Gain</option>
        </select>

        <button onClick={handleSubmit}>
          {loading ? "Generating..." : "Generate Plan"}
        </button>
      </div>

      <div className="card" style={{ whiteSpace: "pre-wrap" }}>
        {result}
      </div>
    </div>
  );
};

export default Diet;