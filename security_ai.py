import os
from google import genai

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Read bandit findings
with open("bandit.txt") as f:
    bandit = f.read()

prompt = f"""
You are a Python security expert.

Convert bandit findings into JSON issues.

Return ONLY JSON array with:
file, line, type (error/warning), message, suggestion

Bandit findings:
{bandit}
"""

res = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=prompt
)

text = res.text.replace("```json","").replace("```","")

with open("ai.json","w") as f:
    f.write(text)

print("Security AI JSON generated")