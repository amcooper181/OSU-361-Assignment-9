# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import trading_pb2 as trading__pb2


class TradingFunctionStub(object):
    """The Trading service definition
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.sendRequest = channel.unary_unary(
                '/trade_server.TradingFunction/sendRequest',
                request_serializer=trading__pb2.ActionRequest.SerializeToString,
                response_deserializer=trading__pb2.ActionReply.FromString,
                )


class TradingFunctionServicer(object):
    """The Trading service definition
    """

    def sendRequest(self, request, context):
        """Function invoked to send the request
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TradingFunctionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'sendRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.sendRequest,
                    request_deserializer=trading__pb2.ActionRequest.FromString,
                    response_serializer=trading__pb2.ActionReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'trade_server.TradingFunction', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TradingFunction(object):
    """The Trading service definition
    """

    @staticmethod
    def sendRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trade_server.TradingFunction/sendRequest',
            trading__pb2.ActionRequest.SerializeToString,
            trading__pb2.ActionReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
