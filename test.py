from bot.client import client
import json

print(client.futures_ping())
print(client.futures_time())

response = client.futures_exchange_info()

print(type(response))
print(response.keys())