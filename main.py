import subprocess

API_KEY = "123456SECRET"  # ❌ Hardcoded secret (LLM review will catch)

def run_cmd(cmd):
    subprocess.Popen(cmd, shell=True)  # ❌ Bandit will flag this

def train(data):
    if data is None:
        print("No data")
        return

    for i in range(len(data)):
        print(data[i])


# Demo calls
run_cmd("ls -la")
train(None)