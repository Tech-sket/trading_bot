# Binance Futures Trading Bot (Testnet)

## 📌 Project Overview

This project is a simplified trading bot built using **Python 3** and the **Binance Futures Testnet**. It allows users to place BUY and SELL orders through a Command Line Interface (CLI).

The bot supports both **MARKET** and **LIMIT** orders and includes input validation, logging, and exception handling.

---

##  Features

- Place MARKET Orders
- Place LIMIT Orders
- BUY & SELL Support
- Binance Futures Testnet Integration
- Command Line Interface (Click)
- Input Validation
- API Request & Response Logging
- Error Handling
- Save API Response to JSON

---

##  Technologies Used

- Python 3.x
- python-binance
- Click
- Python Dotenv
- Requests
- Logging Module

---

##  Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── config.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── logs/
│   ├── market_order.log
│   ├── limit_order.log
│   └── trading.log
│
├── cli.py
├── response.json
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

##  Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/trading_bot.git
```

Move into the project folder.

```bash
cd trading_bot
```

---

### Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

##  Environment Variables

Create a `.env` file.

```
BINANCE_API_KEY=YOUR_API_KEY
BINANCE_API_SECRET=YOUR_API_SECRET
```

> **Note:** Generate API credentials from Binance Futures Testnet.

---

##  Running the Project

### MARKET BUY Order

```bash
python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001
```

---

### MARKET SELL Order

```bash
python cli.py --symbol BTCUSDT --side SELL --order_type MARKET --quantity 0.001
```

---

### LIMIT BUY Order

```bash
python cli.py --symbol BTCUSDT --side BUY --order_type LIMIT --quantity 0.001 --price 50000
```

---

### LIMIT SELL Order

```bash
python cli.py --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.001 --price 120000
```

---

##  Sample Output

```
========================================
ORDER REQUEST
========================================
Symbol       : BTCUSDT
Side         : BUY
Order Type   : MARKET
Quantity     : 0.001

========================================
ORDER RESPONSE
========================================
Order ID      : 19613693686
Status        : FILLED
Executed Qty  : 0.001
Average Price : 108523.45

 Order Placed Successfully
```

---

##  Log Files

The application automatically creates log files inside the `logs` folder.

- trading.log
- market_order.log
- limit_order.log

Logs include:

- API Request
- API Response
- Errors
- Order Details

---

##  Input Validation

The application validates:

- Trading Symbol
- BUY / SELL Side
- MARKET / LIMIT Order Type
- Quantity
- Price (Required for LIMIT Orders)

---

##  Error Handling

The application handles:

- Invalid Symbol
- Invalid Side
- Invalid Quantity
- Invalid Price
- Binance API Errors
- Network Errors
- Unexpected Exceptions

---

##  Requirements

Install all required packages:

```bash
pip install -r requirements.txt
```

---

##  requirements.txt

Example:

```
python-binance
click
python-dotenv
requests
```

---

##  Assumptions

- Binance Futures Testnet account is active.
- API Key and Secret are valid.
- Internet connection is available.
- User has sufficient test balance.

---

##  Assignment Requirements Covered

| Requirement | Status |
|-------------|--------|
| Python 3 | ✅ |
| Binance Futures Testnet | ✅ |
| MARKET Orders | ✅ |
| LIMIT Orders | ✅ |
| BUY | ✅ |
| SELL | ✅ |
| CLI | ✅ |
| Validation | ✅ |
| Logging | ✅ |
| Exception Handling | ✅ |

---

##  Author

Siddhesh patel

Computer Science Engineering Student

---

##  License

This project is developed for educational purposes as part of a technical assignment.