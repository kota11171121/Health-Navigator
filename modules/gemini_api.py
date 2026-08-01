from google import genai

api_key = ""

if api_key != "":
    client = genai.Client(
        api_key=api_key
    )

def get_health_advice(prompt):

    if api_key != "":
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        return response.text

    else:#apiのkeyがない時のアドバイスも書いておく
        return "こんにちは"