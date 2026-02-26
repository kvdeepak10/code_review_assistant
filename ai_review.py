import os

print("AI Review Started...")

# Read main.py as example context
with open("main.py", "r") as f:
    code = f.read()

print("Code sent to AI (simulation)")
print(code[:200])