import json

with open("ai.json") as f:
    try:
        issues = json.load(f)
    except:
        print("Invalid JSON from AI")
        issues = []

# If AI returned string instead of list
if isinstance(issues, str):
    issues = []

for issue in issues:
    if not isinstance(issue, dict):
        continue

    stage = issue.get("stage", "ai")
    level = issue.get("type", "warning")
    file = issue.get("file", "main.py")
    line = issue.get("line", 1)
    msg = issue.get("message", "")
    original = issue.get("original", "")
    suggestion = issue.get("suggestion", "")

    annotation = f"[{stage.upper()}] {msg}"

    if original:
        annotation += f" | Code: {original}"

    if suggestion:
        annotation += f" | Fix: {suggestion}"

    print(f"::{level} file={file},line={line}::{annotation}")
    print(f"{file}:{line}: {level}: {annotation}")