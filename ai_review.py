import os
import requests
from google import genai

print("AI Review Started...")

# ===== Gemini Setup =====
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

with open("main.py", "r") as f:
    code = f.read()

prompt = f"""
You are an expert code reviewer.
Review this code and give clear suggestions:

{code}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

review_text = response.text

print("AI review generated.")

# ===== GitHub Comment Setup =====
repo = os.getenv("GITHUB_REPOSITORY")
token = os.getenv("GITHUB_TOKEN")
run_id = os.getenv("GITHUB_RUN_ID")

url = f"https://api.github.com/repos/{repo}/issues"

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github+json"
}

comment_body = {
    "body": f"## 🤖 AI Code Review\n\n{review_text}"
}

# NOTE:
# For demo we print output (next step we attach to PR)
print("\n===== AI REVIEW =====\n")
print(review_text)