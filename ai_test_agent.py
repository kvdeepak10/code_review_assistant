import os
from google import genai

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Read pytest output
with open("pytest.txt") as f:
    test = f.read()

prompt = f"""
You are a Python testing expert.

Analyze pytest failures and suggest exact code fixes.

Return ONLY valid JSON array.
Do NOT add markdown.
Do NOT add explanation.

Each issue must include:
stage, file, line, type, message, original, suggestion

Rules:
- stage must be "test"
- type must be "error"
- suggestion must fix failing behavior

Pytest output:
{test}
"""

res = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=prompt
)

text = res.text.replace("```json","").replace("```","")

with open("ai.json","w") as f:
    f.write(text)

print("Test AI JSON generated")