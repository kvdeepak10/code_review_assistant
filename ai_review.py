import os
from google import genai

print("AI Review Started...")

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

with open("main.py", "r") as f:
    code = f.read()

prompt = f"""
You are an expert code reviewer.

Analyze this code and provide:
1. Problems found
2. Suggestions
3. Improved code

Code:
{code}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

print("\n==============================")
print("      AI REVIEW REPORT")
print("==============================\n")

print(response.text)

print("\n====== END OF AI REVIEW ======\n")