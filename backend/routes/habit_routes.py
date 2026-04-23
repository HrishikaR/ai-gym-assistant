from flask import Blueprint, request, jsonify
from services.habit_module import add_habit, analyze_habits, get_history

habit_bp = Blueprint("habit", __name__)


@habit_bp.route("/habit/add", methods=["POST"])
def add():
    data = request.get_json()
    day = data.get("day")
    status = data.get("status")

    return jsonify({"message": add_habit(day, status)})


@habit_bp.route("/habit/analyze", methods=["GET"])
def analyze():
    return jsonify({"result": analyze_habits()})


@habit_bp.route("/habit/history", methods=["GET"])
def history():
    return jsonify(get_history())