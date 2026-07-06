import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# Binance Futures Testnet URL
BASE_URL = "https://testnet.binancefuture.com"