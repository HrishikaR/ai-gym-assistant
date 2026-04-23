from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from services.rag_module import get_rag_context
from services.gemini_service import get_ai_response

chat_bp = Blueprint("chat", __name__)


@chat_bp.route("/chat", methods=["POST"])
@cross_origin()
def chat():
    try:
        data = request.get_json()

        # 🔥 SAFE INPUT
        user_message = data.get("message", "")

        if not user_message:
            return jsonify({"response": "Please enter a question"}), 400

        # 🔥 RAG CONTEXT
        context = get_rag_context(user_message)

        prompt = f"""
                You are a professional fitness assistant.

                Using this context:
                {context}

                Answer the user clearly in bullet points.

                User Question: {user_message}
                """

        # 🔥 TRY GEMINI
        try:
            ai_response = get_ai_response(prompt)

        except Exception as e:
            print("Gemini failed:", e)

            # 🔥 FALLBACK (IMPORTANT)
            ai_response = f"""
                    • Based on available data:
                    {context[:300]}

                    • Stay consistent and keep improving!
                    """

        return jsonify({"response": ai_response})

    except Exception as e:
        print("CHAT ERROR:", e)
        return jsonify({"response": "Something went wrong ❌"}), 500