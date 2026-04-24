import google.generativeai as genai
from google import genai
# 🔐 ADD YOUR API KEY HERE
client=genai.Client(api_key="YOUR_API_KEY")



def get_ai_response(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text.strip()
