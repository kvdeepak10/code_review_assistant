import os, json
from google import genai

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

with open("flake.txt") as f:
    flake = f.read()

prompt = f"""
You are a Python code quality expert.

Convert flake8 findings into structured JSON issues.

Return ONLY valid JSON array.
Do NOT add markdown.
Do NOT add explanation.

Each issue must include:
stage, file, line, type, message, original, suggestion

Rules:
- stage must be "quality"
- type must be "warning"
- suggestion must be minimal fix line
- If code should be removed → suggestion = "Remove line"

Flake8 findings:
{flake}
"""


res = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=prompt
)

text = res.text.replace("```json","").replace("```","")

with open("ai.json","w") as f:
    f.write(text)