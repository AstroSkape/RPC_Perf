import logging

import random
import grpc
import mult_pb2
import mult_pb2_grpc
	
def run():
	print("Connecting ...")
	with grpc.insecure_channel('172.17.0.2:50051') as channel:
		stub = mult_pb2_grpc.CalculatorStub(channel)
		payload = '*'*100
		response = stub.Multiply(mult_pb2.CalcRequest(Mat1=payload))
	print("Value received: ", response.value)


if __name__ == '__main__':
    logging.basicConfig()
    run()
