import sys
import uuid
from datetime import datetime
import random
sys.path.append('gen-py')
import os, subprocess
import cProfile, pstats
import resource, psutil
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from pyinstrument import Profiler
from pyinstrument.session import Session
from pyinstrument.renderers import ConsoleRenderer

from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
#from contact import ContactSvc, ttypes
from mult import MultiplicationService, ttypes
	
socket = TSocket.TSocket('192.168.100.4', 9090)
transport = TTransport.TFramedTransport(socket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = MultiplicationService.Client(protocol)

transport.open()

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


def main():
	pid = os.getpid()
	#subprocess.run(["bash", "cpu_usage.sh", str(pid)])
	#os.system("bash cpu_usage.sh "+str(pid))
	#print(resource.getrusage(resource.RUSAGE_SELF)[0], resource.getrusage(resource.RUSAGE_SELF)[1], resource.getrusage(resource.RUSAGE_SELF)[3], resource.getrusage(resource.RUSAGE_SELF)[4])
	payload = '*'*4194299
	#result = client.multiply(payload)
	with ThreadPoolExecutor() as executor:
		monitor = MemoryMonitor()
		mem_thread = executor.submit(monitor.measure_usage)
		try:
			fn_thread = executor.submit(client.multiply, payload)
			result = fn_thread.result()
		finally:
			monitor.keep_measuring = False
			max_mem, max_user, max_sys = mem_thread.result()
			
		print(f"Peak memory usage: {max_mem}kB")
		print(f"Peak user time: {max_user}s, Peak system time: {max_sys}s")
	profiler = Profiler()
	profiler.start()
	result = client.multiply(payload)
	session = profiler.stop()
	print(ConsoleRenderer(unicode=True, color=True, show_all=True).render(session))
	print("Payload size:", len(payload))
	print(result)



if __name__ == '__main__':
	
	#profiler = cProfile.Profile()
	#profiler.enable()
	main()
	#profiler.disable()
	#stats = pstats.Stats(profiler).sort_stats('cumtime')
	#stats.print_stats()
