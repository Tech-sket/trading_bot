import click
import json
from bot.orders import OrderManager
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)


@click.command()
@click.option("--symbol", required=True, help="Trading Symbol (BTCUSDT)")
@click.option("--side", required=True, help="BUY or SELL")
@click.option("--order_type", required=True, help="MARKET or LIMIT")
@click.option("--quantity", required=True, type=float)
@click.option("--price", required=False, type=float)

def main(symbol, side, order_type, quantity, price):

    try:

        symbol = validate_symbol(symbol)
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)

        if order_type == "LIMIT":
            price = validate_price(price)

        print("\n========================================")
        print("          ORDER REQUEST")
        print("========================================")
        print(f"Symbol       : {symbol}")
        print(f"Side         : {side}")
        print(f"Order Type   : {order_type}")
        print(f"Quantity     : {quantity}")

        if order_type == "LIMIT":
            print(f"Price        : {price}")

        print("========================================")

        response = OrderManager.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        with open("response.json", "w") as file:
            json.dump(response, file, indent=4)

        print("\n========================================")
        print("          ORDER RESPONSE")
        print("========================================")

        print("Order ID      :", response.get("orderId", "N/A"))
        print("Status        :", response.get("status", "N/A"))
        print("Executed Qty  :", response.get("executedQty", "N/A"))
        print("Original Qty  :", response.get("origQty", "N/A"))
        print("Average Price :", response.get("avgPrice", "N/A"))
        print("Side          :", response.get("side", "N/A"))
        print("Symbol        :", response.get("symbol", "N/A"))

        print("========================================")
        print("✅ Order Placed Successfully")

    except Exception as e:

        print("\n❌ ERROR")
        print(e)


if __name__ == "__main__":
    main()