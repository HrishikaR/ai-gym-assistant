from services.gemini_service import get_ai_response
from database.db import habit_collection


# 🔹 Add habit
def add_habit(day, status):
    entry = {
        "day": day,
        "status": status
    }

    habit_collection.insert_one(entry)

    return "Habit saved to DB ✅"


# 🔹 Get history
def get_history():
    data = list(habit_collection.find({}, {"_id": 0}))
    return data


# 🔹 Analyze habits
def analyze_habits():
    habits = list(habit_collection.find())

    total_days = len(habits)

    if total_days == 0:
        return "No data available"

    completed = sum(1 for h in habits if h["status"] == "done")
    missed = total_days - completed

    consistency = (completed / total_days) * 100

    if consistency < 40:
        risk = "High risk ❌"
        fallback = "Start small and be consistent."
    elif consistency < 70:
        risk = "Moderate ⚠️"
        fallback = "Improve consistency."
    else:
        risk = "Strong habit ✅"
        fallback = "Great job!"

    try:
        prompt = f"""
        Habit Data:
        Consistency: {consistency:.2f}%

        Give short motivation and suggestion.
        """

        ai_feedback = get_ai_response(prompt)

    except:
        ai_feedback = f"""
        • Consistency: {consistency:.2f}%
        • {fallback}
        • Stay disciplined!
        """

    return f"""
        📊 Habit Analysis:

        Consistency: {consistency:.2f}%
        {risk}

        🤖 Feedback:
        {ai_feedback}
        """