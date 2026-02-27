import os, json
from google import genai

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

with open("flake.txt") as f:
    flake = f.read()

prompt = f"""
You are a Python code quality expert.

You will receive flake8 findings.

Convert them into structured JSON issues.

Rules:
- Return ONLY JSON array
- Each issue must contain:
  file, line, type (warning), message, suggestion
- Suggest minimal replacement line or "Remove line"

Flake8 findings:
{flake}
"""


res = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

text = res.text.replace("```json","").replace("```","")

with open("ai.json","w") as f:
    f.write(text)