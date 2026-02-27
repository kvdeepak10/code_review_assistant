import os
import json
from google import genai

print("AI Review Started...")

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Read code
with open("main.py", "r") as f:
    code = f.read()

prompt = f"""
You are an expert Python reviewer.

Return ONLY valid JSON array.

Each issue must contain:
file, line, type (error/warning), message, suggestion

Suggestion must be minimal fix line.

Code:
{code}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

# Clean Gemini markdown
text = response.text.strip()
text = text.replace("```json", "").replace("```", "")

# Save output
with open("ai.json", "w") as f:
    f.write(text)

print("AI JSON saved")