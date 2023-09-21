import os

from app import create_app
from app.person.services import PersonService
import grpc
from app.protos import person_pb2
from app.protos import person_pb2_grpc
from concurrent import futures

app = create_app(os.getenv("FLASK_ENV") or "test")

grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
person_pb2_grpc.add_PersonServiceServicer_to_server(PersonService(), grpc_server)
grpc_server.add_insecure_port("localhost:5005")

if __name__ == "__main__":
    grpc_server.start()
    app.run(debug=True)
