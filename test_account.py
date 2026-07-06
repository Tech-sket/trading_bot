from bot.client import client
import json

try:
    account = client.futures_account()

    print(json.dumps(account, indent=4))

except Exception as e:
    print("ERROR:")
    print(e)
    