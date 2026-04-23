const Trainer = () => {
  return (
    <div style={{
      minHeight: "100vh",
      background: "#0f172a",
      color: "white",
      textAlign: "center",
      padding: "20px"
    }}>
      <h1>🏋️ AI Gym Trainer</h1>

      <div style={{
        display: "flex",
        justifyContent: "center",
        marginTop: "20px"
      }}>
        <div style={{
          width: "90%",
          maxWidth: "800px",
          borderRadius: "15px",
          overflow: "hidden",
          boxShadow: "0px 4px 20px rgba(0,0,0,0.4)"
        }}>
          <img
            src="http://127.0.0.1:5000/video_feed"
            alt="trainer"
            style={{
              width: "100%",
              height: "auto",
              display: "block"
            }}
          />
        </div>
      </div>
    </div>
  );
};

export default Trainer;