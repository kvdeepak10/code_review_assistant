import os, json
from google import genai

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

with open("flake.txt") as f:
    flake = f.read()

prompt = f"""
You are a Python code quality expert.

Convert flake8 findings into JSON issues.

Return JSON:
[file, line, type, message, suggestion]

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