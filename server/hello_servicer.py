from concurrent import futures

import grpc
import hello_pb2
import hello_pb2_grpc

class HelloServicer(hello_pb2_grpc.HelloServiceServicer):
    def SayHello(self, request, context):
        return hello_pb2.HelloResponse(message="Hello, %s!!" % request.name)

