import json

print("\n🔧 Fix Agent Started...\n")

# Load AI report
with open("ai.json") as f:
    issues = json.load(f)

# Display fixes
for issue in issues:
    file = issue.get("file")
    line = issue.get("line")
    msg = issue.get("message")
    original = issue.get("original")
    suggestion = issue.get("suggestion")

    print(f"File: {file}")
    print(f"Line: {line}")
    print(f"Issue: {msg}")
    print(f"Original: {original}")
    print(f"Suggested Fix: {suggestion}")
    print("-" * 40)