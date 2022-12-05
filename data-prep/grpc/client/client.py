import logging
import sys
import random
import grpc
import mult_pb2
import mult_pb2_grpc
from pyinstrument import Profiler
from pyinstrument.renderers import ConsoleRenderer
	
def run():
	print("Connecting ...")
	with grpc.insecure_channel('localhost:50051') as channel:
		stub = mult_pb2_grpc.CalculatorStub(channel)
		print(sys.argv[1])
		times = int(sys.argv[1])
		payload = '*'*times
		profiler = Profiler()
		profiler.start()
		response = stub.Multiply(mult_pb2.CalcRequest(Mat1=payload))
		session = profiler.stop()
		print(ConsoleRenderer(unicode=True, color=False, show_all=True).render(session))
	print("Value received: ", response.value)


if __name__ == '__main__':
    logging.basicConfig()
    run()
