import logging

import random
import grpc
import sys
import mult_pb2
import mult_pb2_grpc
import os, resource
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from pyinstrument import Profiler
from pyinstrument.session import Session
from pyinstrument.renderers import ConsoleRenderer

class MemoryMonitor:
	def __init__(self):
		self.keep_measuring = True

	def measure_usage(self):
		max_mem = 0
		max_user = 0
		max_sys = 0
		while self.keep_measuring:
			max_mem = max(
                max_mem,
                resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            )
			max_user = max(
                max_user,
                resource.getrusage(resource.RUSAGE_SELF).ru_utime
				#psutil.cpu_percent()
			)
			max_sys = max(
                max_sys,
                resource.getrusage(resource.RUSAGE_SELF).ru_stime
            )
			sleep(0.1)
			
		return max_mem, max_user, max_sys
	
def run():
	#print("Connecting ...")
	with grpc.insecure_channel('localhost:50051') as channel:
		stub = mult_pb2_grpc.CalculatorStub(channel)
		size = int(sys.argv[1])
		payload = '*'*size
		#response = stub.Multiply(mult_pb2.CalcRequest(Mat1=payload))
		with ThreadPoolExecutor() as executor:
			monitor = MemoryMonitor()
			mem_thread = executor.submit(monitor.measure_usage)
			try:
				fn_thread = executor.submit(stub.Multiply, mult_pb2.CalcRequest(Mat1=payload))
				result = fn_thread.result()
			finally:
				monitor.keep_measuring = False
				max_mem, max_user, max_sys = mem_thread.result()
				
			#print(f"Peak memory usage: {max_mem}kB")
			#print(f"Peak user time: {max_user}s, Peak system time: {max_sys}s")
			print(max_mem, max_user, max_sys)
	#print("Value received: ", result.value)


if __name__ == '__main__':
	logging.basicConfig()
	run()
