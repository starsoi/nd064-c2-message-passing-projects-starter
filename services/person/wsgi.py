import os

import grpc
from app.protos import person_pb2
from app.protos import person_pb2_grpc
from concurrent import futures
from app.person.services import PersonService

grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
person_pb2_grpc.add_PersonServiceServicer_to_server(PersonService(), grpc_server)
grpc_server.add_insecure_port("localhost:5005")
print('gRPC server starting...')
grpc_server.start()
print('gRPC server started')

from app import create_app
print('create app')
app = create_app(os.getenv("FLASK_ENV") or "test")


if __name__ == "__main__":
    print('start app')
    app.run(debug=True)
    print('app exit')
