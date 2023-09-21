# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import person_pb2 as person__pb2


class PersonServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RetreaveAll = channel.unary_unary(
                '/PersonService/RetreaveAll',
                request_serializer=person__pb2.Empty.SerializeToString,
                response_deserializer=person__pb2.Persons.FromString,
                )


class PersonServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RetreaveAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PersonServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RetreaveAll': grpc.unary_unary_rpc_method_handler(
                    servicer.RetreaveAll,
                    request_deserializer=person__pb2.Empty.FromString,
                    response_serializer=person__pb2.Persons.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'PersonService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PersonService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RetreaveAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PersonService/RetreaveAll',
            person__pb2.Empty.SerializeToString,
            person__pb2.Persons.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
