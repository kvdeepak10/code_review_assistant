import json

with open("ai.json") as f:
    issues = json.load(f)

for issue in issues:
    stage = issue.get("stage","ai")
    level = issue["type"]
    file = issue["file"]
    line = issue["line"]
    msg = issue["message"]
    original = issue.get("original","")
    suggestion = issue.get("suggestion","")

    annotation = f"[{stage.upper()}] {msg}"

    if original:
        annotation += f" | Code: {original}"

    if suggestion:
        annotation += f" | Fix: {suggestion}"

    print(f"::{level} file={file},line={line}::{annotation}")