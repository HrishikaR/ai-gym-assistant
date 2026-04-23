import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Diet from "./pages/Diet";
import Chat from "./pages/Chat";
import Habit from "./pages/Habit";
import Trainer from "./pages/Trainer";
import Analytics from "./pages/Analytics";


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/diet" element={<Diet />} />
        <Route path="/chat" element={<Chat />} />
        <Route path="/habit" element={<Habit />} />
        <Route path="/trainer" element={<Trainer />} />
        <Route path="/analytics" element={<Analytics />} />
      </Routes>
    </Router>
  );
}

export default App;