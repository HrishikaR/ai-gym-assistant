from services.rag_module import get_rag_context
from services.gemini_service import get_ai_response

# 🔥 Simple in-memory tracking (can later upgrade to DB)
nutrition_history = []


def calculate_bmi(weight, height):
    height_m = height / 100
    return round(weight / (height_m ** 2), 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def calculate_calories(weight, height, age, goal):
    bmr = 10 * weight + 6.25 * height - 5 * age + 5

    if goal == "loss":
        return int(bmr - 300)
    elif goal == "gain":
        return int(bmr + 300)
    return int(bmr)


# 🔥 MAIN FUNCTION
def get_diet_plan(weight, height, age, goal):
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)
    calories = calculate_calories(weight, height, age, goal)

    query = f"{goal} diet plan {calories} calories"

    context = get_rag_context(query)

    prompt = f"""
                You are a professional dietician.

                Using this context:
                {context}

                Generate:
                1. Diet plan (Breakfast, Lunch, Dinner)
                2. Grocery list (simple items)

                Keep output clean and structured in bullet points.
                """

    # 🔥 TRY LLM → FALLBACK TO RAG
    try:
        response = get_ai_response(prompt)

    except Exception as e:
        print("LLM failed, using RAG fallback:", e)

        response = f"""
                🥗 Diet Plan (from knowledge base):

                {context[:500]}
                """

    return f"""
            📊 BMI: {bmi} ({category})

            🔥 Calories: {calories} kcal/day

            🥗 Diet & Grocery Plan:
            {response}
            """.strip()


# 🔥 NEW: Track nutrition intake
def track_nutrition(food, calories):
    entry = {
        "food": food,
        "calories": calories
    }

    nutrition_history.append(entry)

    total = sum(item["calories"] for item in nutrition_history)

    return f"""
            ✅ Added: {food} ({calories} kcal)

            🔥 Total Intake Today: {total} kcal
            """