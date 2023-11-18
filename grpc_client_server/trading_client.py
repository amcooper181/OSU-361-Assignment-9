import grpc
import trading_pb2_grpc as pb2_grpc
import trading_pb2 as pb2

class TradingClient(object):
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        self.channel = grpc.insecure_channel(
                '{}:{}'.format(self.host, self.server_port))

        self.stub = pb2_grpc.TradingFunctionStub(self.channel)

    def get_url(self, request_type, symbol, quantity):

        message = pb2.ActionRequest(request_type=request_type, symbol=symbol, quantity=quantity)
        print(f'{message}')
        return self.stub.sendRequest(message)

if __name__ == "__main__":
    client = TradingClient()
    result = client.get_url('buy', 'TSLA', 3)
    print(f'{result}')

