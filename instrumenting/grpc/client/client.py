import logging

import random
import grpc
import mult_pb2
import mult_pb2_grpc
import os, resource
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from pyinstrument import Profiler
from pyinstrument.session import Session
from pyinstrument.renderers import ConsoleRenderer

	
def run():
	print("Connecting ...")
	with grpc.insecure_channel('localhost:50051') as channel:
		stub = mult_pb2_grpc.CalculatorStub(channel)
		payload = '*'*4194299
		response = stub.Multiply(mult_pb2.CalcRequest(Mat1=payload))
	#print("Value received: ", response.value)


if __name__ == '__main__':
	logging.basicConfig()
	profiler = Profiler()
	profiler.start()
	run()
	session = profiler.stop()
	print(ConsoleRenderer(unicode=True, color=True, show_all=True).render(session))
