from bot.client import client
import json

try:
    response = client.futures_create_order(
        symbol="BTCUSDT",
        side="BUY",
        type="MARKET",
        quantity=0.001
    )

    print(json.dumps(response, indent=4))

except Exception as e:
    print("ERROR:")
    print(e)