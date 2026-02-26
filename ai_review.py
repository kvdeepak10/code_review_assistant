import os
import google.generativeai as genai

print("AI Review Started...")

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

# Read code context
with open("main.py", "r") as f:
    code = f.read()

prompt = f"""
You are an expert code reviewer.

Analyze this Python code and give:

1. Problems found
2. Suggestions to improve
3. Corrected code example

Code:
{code}
"""

response = model.generate_content(prompt)

# Save AI report
with open("review_report.md", "w") as f:
    f.write(response.text)

print("AI review report generated.")