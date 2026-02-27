API_KEY = "123456SECRET"   # ❌ Hardcoded secret (intentional)

def train(data):

    if data == None:
        print("No data")

    x = 10  # unused variable

    for i in range(len(data)):
        print(data[i])


train(None)