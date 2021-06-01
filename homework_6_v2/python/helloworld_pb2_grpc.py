# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import helloworld_pb2 as helloworld__pb2


class NotificatorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.subscribe = channel.unary_stream(
                '/helloworld.Notificator/subscribe',
                request_serializer=helloworld__pb2.Subscription.SerializeToString,
                response_deserializer=helloworld__pb2.Notification.FromString,
                )


class NotificatorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def subscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NotificatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.subscribe,
                    request_deserializer=helloworld__pb2.Subscription.FromString,
                    response_serializer=helloworld__pb2.Notification.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'helloworld.Notificator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Notificator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/helloworld.Notificator/subscribe',
            helloworld__pb2.Subscription.SerializeToString,
            helloworld__pb2.Notification.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
