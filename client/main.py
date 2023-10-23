from __future__ import print_function

import grpc
import hello_pb2
import hello_pb2_grpc

def run():
    print("client start...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = hello_pb2_grpc.HelloServiceStub(channel)
        response = stub.SayHello(hello_pb2.HelloRequest(name="Bob"))
    
    print("cliet received: " + response.message)

if __name__ == "__main__":
    run()