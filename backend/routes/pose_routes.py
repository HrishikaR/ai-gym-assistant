from flask import Blueprint
from flask import Blueprint, Response


pose_bp = Blueprint('pose', __name__)
@pose_bp.route("/video_feed")
def video_feed():
    from services.pose_module import generate_frames  # 🔥 lazy import
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')



