import subprocess

# ❌ Hardcoded secret (LLM Review Agent should flag this)
API_KEY = "123456SECRET"


def run_cmd(cmd):
    """
    Runs a shell command.
    ❌ Bandit should flag shell=True as a security risk (shell injection)
    """
    subprocess.Popen(cmd, shell=True)


def train(data):
    """
    Simple training loop demo.
    Quality agent may suggest logging instead of print.
    """
    if data is None:
        print("No data provided")  # LLM review may suggest logging
        return

    for i in range(len(data)):
        print(data[i])


def greet(name):
    """
    Runtime safety issue — pytest or LLM may suggest validation.
    """
    print("Hello " + name)


# =====================
# Demo calls (CI should catch issues)
# =====================
run_cmd("ls -la")       # ❌ security risk
train(None)             # edge case
greet(None)             # runtime issue