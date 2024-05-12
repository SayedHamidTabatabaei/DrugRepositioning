from concurrent import futures

import grpc

from businesses import migration_data_business
from configs import config
from protos.generated import drug_data_pb2_grpc, drug_data_pb2


class DrugDataService(drug_data_pb2_grpc.DrugDataService):
    def __init__(self):
        self.migration_data_business = migration_data_business.MigrationDataBusiness()

    def MigrateData(self, request, context, **kwargs):
        try:
            self.migration_data_business.start(request.file_name)

            return drug_data_pb2.StatusModel(status=True, message='Insert data successfully!')

        except Exception as e:
            return drug_data_pb2.StatusModel(status=False, message='Insert data failed!')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=(('grpc.so_reuseport', 0),))
    drug_data_pb2_grpc.add_DrugDataServiceServicer_to_server(DrugDataService(), server)
    server.add_insecure_port(config.data_process_service_address)
    server.start()
    server.wait_for_termination(timeout=7200)


if __name__ == '__main__':
    serve()
