# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import drug_data_pb2 as drug__data__pb2

GRPC_GENERATED_VERSION = '1.63.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in drug_data_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class DrugDataServiceStub(object):
    """import "enums.proto";

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MigrateData = channel.unary_unary(
                '/DrugDataService/MigrateData',
                request_serializer=drug__data__pb2.MigrateDataRequest.SerializeToString,
                response_deserializer=drug__data__pb2.MigrateDataResponse.FromString,
                _registered_method=True)


class DrugDataServiceServicer(object):
    """import "enums.proto";

    """

    def MigrateData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DrugDataServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MigrateData': grpc.unary_unary_rpc_method_handler(
                    servicer.MigrateData,
                    request_deserializer=drug__data__pb2.MigrateDataRequest.FromString,
                    response_serializer=drug__data__pb2.MigrateDataResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DrugDataService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DrugDataService(object):
    """import "enums.proto";

    """

    @staticmethod
    def MigrateData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/DrugDataService/MigrateData',
            drug__data__pb2.MigrateDataRequest.SerializeToString,
            drug__data__pb2.MigrateDataResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
