import os
from google import genai

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Read code
with open("main.py") as f:
    code = f.read()

prompt = f"""
You are a senior Python reviewer.

Analyze the code and provide improvement suggestions.

Return ONLY JSON array with:
file, line, type (warning), message, suggestion

Focus on:
- Refactoring
- Best practices
- Performance
- Readability
- Logging vs print
- Type hints

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