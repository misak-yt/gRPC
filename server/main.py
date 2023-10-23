from hello_pb2_grpc import add_HelloServiceServicer_to_server
from hello_servicer import HelloServicer
from concurrent import futures
import grpc

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    add_HelloServiceServicer_to_server(HelloServicer(), server)
    server.add_insecure_port('localhost:' + port)
    server.start()
    print('server started, listening on ' + port)
    server.wait_for_termination()

if __name__ == "__main__":
    serve()