import json

with open("ai.json") as f:
    issues = json.load(f)

for issue in issues:
    level = issue["type"]
    file = issue["file"]
    line = issue["line"]
    msg = issue["message"]
    suggestion = issue["suggestion"]

    print(f"::{level} file={file},line={line}::{msg} | Fix: {suggestion}")