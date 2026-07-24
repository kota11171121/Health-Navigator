from google import genai

client = genai.Client(api_key="")

prompt = """
BMIは22.5
血圧138/86
徒歩30分

200文字以内で健康アドバイスを書いてください。
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)