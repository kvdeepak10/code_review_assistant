import os
from google import genai

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Read pytest output
with open("pytest.txt") as f:
    test = f.read()

prompt = f"""
You are a Python testing expert.

Analyze pytest failures and convert them into JSON issues.

Return ONLY JSON array with:
file, line, type (error), message, suggestion

Pytest output:
{test}
"""

res = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

text = res.text.replace("```json","").replace("```","")

with open("ai.json","w") as f:
    f.write(text)

print("Test AI JSON generated")