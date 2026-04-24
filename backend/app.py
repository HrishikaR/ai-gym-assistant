from flask import Flask
from flask_cors import CORS
import os

# ✅ Import only safe modules first
from routes.chatbot_routes import chat_bp
from routes.diet_routes import diet_bp
from routes.habit_routes import habit_bp

app = Flask(__name__)
CORS(app)

# ✅ Register working modules ONLY ONCE
app.register_blueprint(chat_bp)
app.register_blueprint(diet_bp)
app.register_blueprint(habit_bp)

# 🔥 SAFE LOAD pose module (NO crash)
try:
    from routes.pose_routes import pose_bp
    app.register_blueprint(pose_bp)
    print("Pose module loaded ✅")
except Exception as e:
    print("Pose module skipped (cloud env) ❌:", e)


@app.route('/')
def home():
    return {"message": "AI Gym Assistant Backend Running"}


# 🔥 IMPORTANT FOR RENDER
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
