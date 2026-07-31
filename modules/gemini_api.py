from google import genai

client = genai.Client(
    api_key=""
)

def get_health_advice(prompt):

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text