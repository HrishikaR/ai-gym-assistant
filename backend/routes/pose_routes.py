from flask import Blueprint
from flask import Blueprint, Response
from services.pose_module import generate_frames

pose_bp = Blueprint('pose', __name__)



@pose_bp.route("/video_feed")
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')