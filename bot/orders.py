from time import sleep
from binance.exceptions import BinanceAPIException
from bot.client import client
from bot.logging_config import logger


class OrderManager:

    @staticmethod
    def place_order(symbol, side, order_type, quantity, price=None):

        try:

            params = {
                "symbol": symbol.upper(),
                "side": side.upper(),
                "type": order_type.upper(),
                "quantity": quantity,
                "newOrderRespType": "RESULT"
            }

            if order_type.upper() == "LIMIT":
                params["price"] = price
                params["timeInForce"] = "GTC"

            logger.info(f"Order Request: {params}")

            # Place Order
            response = client.futures_create_order(**params)

            logger.info(f"Initial Response: {response}")

            order_id = response["orderId"]

            # Wait a second so Binance updates the order status
            sleep(1)

            # Fetch latest order information
            final_response = client.futures_get_order(
                symbol=symbol.upper(),
                orderId=order_id
            )

            logger.info(f"Final Response: {final_response}")

            return final_response

        except BinanceAPIException as e:
            logger.error(e.message)
            raise Exception(e.message)

        except Exception as e:
            logger.error(str(e))
            raise Exception(str(e))