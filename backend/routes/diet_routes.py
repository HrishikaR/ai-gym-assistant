from flask import Blueprint, request, jsonify
from services.diet_module import get_diet_plan,track_nutrition

diet_bp = Blueprint('diet', __name__)

@diet_bp.route('/diet', methods=['POST'])
def diet():
    data = request.get_json()

    weight = int(data.get("weight"))
    height = int(data.get("height"))
    age = int(data.get("age"))
    goal = data.get("goal") # loss / gain

    if not all([weight, height, age, goal]):
        return jsonify({"error": "Missing inputs"}), 400

    result = get_diet_plan(weight, height, age, goal)

    return jsonify({"result": result})

@diet_bp.route('/track', methods=['POST'])
def track():
    try:
        data = request.get_json()

        food = data.get("food")
        calories = data.get("calories")

        if not food or not calories:
            return jsonify({"error": "Missing food or calories"}), 400

        result = track_nutrition(food, calories)

        return jsonify({
            "status": "success",
            "result": result
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
    
@diet_bp.route('/diet', methods=['POST'])
def get_diet():
    data = request.get_json()
    print("DATA RECEIVED:", data)  # 👈 ADD THIS