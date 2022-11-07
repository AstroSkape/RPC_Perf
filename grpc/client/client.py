import logging

import grpc
import mult_pb2
import mult_pb2_grpc


def run():
    print("Connecting ...")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = mult_pb2_grpc.CalculatorStub(channel)
        response = stub.Multiply(mult_pb2.CalcRequest(num1=2,num2=3))
    print("Value received: ", response.value)


if __name__ == '__main__':
    logging.basicConfig()
    run()