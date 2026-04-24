from flask import Flask
from flask_cors import CORS
from routes.pose_routes import pose_bp
from routes.chatbot_routes import chat_bp
from routes.diet_routes import diet_bp
from routes.habit_routes import habit_bp
from routes.pose_routes import pose_bp
import os
app = Flask(__name__)
CORS(app)



app.register_blueprint(pose_bp)
app.register_blueprint(chat_bp)

app.register_blueprint(diet_bp)
app.register_blueprint(habit_bp)

@app.route('/')
def home():
    return {"message": "AI Gym Assistant Backend Running"}

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
