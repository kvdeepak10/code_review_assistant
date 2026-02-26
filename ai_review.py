import os
import google.generativeai as genai

print("AI Review Started...")

# Read API key from environment (GitHub pipeline passes this)
api_key = os.getenv("GOOGLE_API_KEY")

print("API KEY FOUND:", bool(api_key))

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found!")

# Configure Gemini
genai.configure(api_key=api_key)

# Create model
model = genai.GenerativeModel("gemini-2.5-flash-lite")

# Read code to review
with open("main.py", "r") as f:
    code = f.read()

prompt = f"""
You are an expert code reviewer.

Analyze this Python code and provide:

1. Problems found
2. Suggestions for improvement
3. Corrected code example

Code:
{code}
"""

# Ask Gemini
response = model.generate_content(prompt)

print("\n==============================")
print("      AI REVIEW REPORT")
print("==============================\n")

print(response.text)

print("\n====== END OF AI REVIEW ======\n")