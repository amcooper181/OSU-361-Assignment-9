import requests
from concurrent import futures
import time
import grpc
import trading_pb2_grpc as pb2_grpc
import trading_pb2 as pb2


BASE_URL = "https://paper-api.alpaca.markets/v2/"

API_KEY = ""
SECRET_KEY = ""


class TradingFunctionService(pb2_grpc.TradingFunctionServicer):
    
    def __init__(self) -> None:
        pass

    def sendRequest(self, request, context):
        request_type = request.request_type
        symbol = request.symbol
        quantity = request.quantity
        reply_msg = str(self.wrapper_function(API_KEY, SECRET_KEY, request_type, symbol, quantity))
        return pb2.ActionReply(reply_msg = reply_msg)

    def place_order(self, api_key, secret_key, symbol, quantity, side):  # buy or sell order function
        url = BASE_URL + "orders"

        payload = {
            "symbol": symbol,
            "qty": quantity,
            "side": side,
            "type": "market",
            "time_in_force": "day"
        }

        headers = {
            "APCA-API-KEY-ID": api_key,
            "APCA-API-SECRET-KEY": secret_key,
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)
        return response.json()

    def get_open_buy_orders(self, api_key, secret_key): # buy function
        url = BASE_URL + "orders"

        headers = {
            "APCA-API-KEY-ID": api_key,
            "APCA-API-SECRET-KEY": secret_key,
            "accept": "application/json"
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            orders = response.json()
            return [order for order in orders if order["side"] == "buy"]
        else:
            print(f"Error fetching open orders. Status code: {response.status_code}")
            return None

    def get_open_sell_orders(self, api_key, secret_key): # sell function
        url = BASE_URL + "orders"
        headers = {
            "APCA-API-KEY-ID": api_key,
            "APCA-API-SECRET-KEY": secret_key,
            "accept": "application/json"
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            orders = response.json()
            return [order for order in orders if order["side"] == "sell"]
        else:
            print(f"Error fetching open orders. Status code: {response.status_code}")
            return None

    def delete_order(self, api_key, secret_key, order_id): # delete by id
        url = BASE_URL + f"orders/{order_id}"
        headers = {
            "APCA-API-KEY-ID": api_key,
            "APCA-API-SECRET-KEY": secret_key
        }
        response = requests.delete(url, headers=headers)

        if response.status_code == 204:
            print(f"Successfully canceled the order with the ID {order_id}")
        else:
            print(f"Error canceling the order with the ID {order_id}. Status code: {response.status_code}")

    def get_open_positions(self, api_key, secret_key):
        url = BASE_URL + "positions"
        headers = {
            "APCA-API-KEY-ID": api_key,
            "APCA-API-SECRET-KEY": secret_key,
            "accept": "application/json"
        }
        response = requests.get(url, headers=headers)
        return response.json()

    def get_open_orders(self, api_key, secret_key):
        url = BASE_URL + "orders"
        headers = {
            "APCA-API-KEY-ID": api_key,
            "APCA-API-SECRET-KEY": secret_key,
            "accept": "application/json"
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            orders = response.json()
            if not orders:
                print("No open orders.")
            else:
                print("Open Orders:")
                for order in orders:
                    print(order)
            return orders
        else:
            print(f"Error fetching open orders. Status code: {response.status_code}")
            return None

    def get_account_positions(self, api_key, secret_key):
        url = BASE_URL + "positions"
        headers = {
            "APCA-API-KEY-ID": api_key,
            "APCA-API-SECRET-KEY": secret_key,
            "accept": "application/json"
        }

        response = requests.get(url, headers=headers)
        return response.json()

    def wrapper_function(self, api_key, secret_key, request_type, symbol, quantity):
        if request_type in ["buy", "sell"]:
            result = self.place_order(api_key, secret_key, symbol, quantity, request_type)
        
        elif request_type == "positions":
            result = self.get_account_positions(api_key, secret_key)
        
        elif request_type == "orders":
            result = self.get_open_orders(api_key, secret_key)
        
        elif request_type == "cancel_buy":
            open_orders = self.get_open_orders(api_key, secret_key)
            if open_orders:
                print("Open orders found. Cancelling as requested...")
                for order in open_orders:
                    self.delete_order(api_key, secret_key, order['id'])
            else:
                print("No open orders to cancel.")
        
        elif request_type == "cancel_sell":
            open_sell_orders = self.get_open_sell_orders(api_key, secret_key)
            if open_sell_orders:
                print("Open sell orders found. Cancelling as requested...")
                for order in open_sell_orders:
                    self.delete_order(api_key, secret_key, order['id'])
            else:
                print("No open sell orders to cancel.")
        else:
            result = None

        return result

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_TradingFunctionServicer_to_server(TradingFunctionService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()

# source: https://docs.alpaca.markets/reference/postorder
# source: https://docs.alpaca.markets/reference/getallopenpositions
# source: https://docs.alpaca.markets/reference/getallorders
