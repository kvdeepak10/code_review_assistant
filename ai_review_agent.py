import os
from google import genai

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Read code
with open("main.py") as f:
    code = f.read()

prompt = f"""
You are a senior Python reviewer.

Provide line-level improvement suggestions.

Return ONLY valid JSON array.
Do NOT add markdown.
Do NOT add explanation.

Each issue must include:
stage, file, line, type, message, original, suggestion

Rules:
- stage must be "review"
- type must be "warning"
- Focus on readability, best practices, refactoring

The file name is main.py.

Code:
{code}
"""

res = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=prompt
)

text = res.text.replace("```json","").replace("```","")

with open("ai.json","w") as f:
    f.write(text)

print("Review AI JSON generated")