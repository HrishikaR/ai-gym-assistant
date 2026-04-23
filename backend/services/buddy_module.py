from services.rag_module import get_rag_context
from services.gemini_service import get_ai_response


# 🔥 Emotion detection
def detect_emotion(query):
    query = query.lower()

    if any(word in query for word in ["tired", "lazy", "no energy", "sad"]):
        return "low"
    elif any(word in query for word in ["motivated", "excited", "happy"]):
        return "high"
    else:
        return "neutral"


# 🔥 Main chatbot
def get_buddy_response(query):
    emotion = detect_emotion(query)
    query_lower = query.lower()

    context = get_rag_context(query)

    # 🔥 Detect intent (simple but effective)
    if any(word in query_lower for word in ["workout", "exercise", "training"]):
        intent = "workout"
    elif any(word in query_lower for word in ["diet", "food", "eat"]):
        intent = "diet"
    else:
        intent = "general"

    # 🔥 Emotion tone
    if emotion == "low":
        tone = "Be very motivating and encouraging"
    elif emotion == "high":
        tone = "Be energetic and supportive"
    else:
        tone = "Be helpful and structured"

    prompt = f"""
                You are a smart AI gym assistant.

                User emotion: {emotion}
                Instruction: {tone}

                Use this context:
                {context}

                Respond:
                - Bullet points
                - Clean format
                - Relevant to user query
                """

    try:
        return get_ai_response(prompt)

    except:
        # 🔥 INTELLIGENT FALLBACK

        if intent == "workout":
            return """
                💪 Basic Workout Plan:

                • Squats – 3×10  
                • Push-ups – 3×8  
                • Lunges – 3×10  
                • Plank – 30 sec  

                🔥 Do 3–4 times/week
                """.strip()

        elif intent == "diet":
            return """
                🥗 Simple Diet Plan:

                • Breakfast: Oats + fruits  
                • Lunch: Rice + vegetables + protein  
                • Dinner: Salad + light protein  

                💧 Drink plenty of water
                """.strip()

        elif emotion == "low":
            return """
            🔥 You’ve got this!

            • Start small  
            • Don’t skip today  
            • Progress > perfection  
            """.strip()

        else:
            return "Stay consistent and keep improving!"