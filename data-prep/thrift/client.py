import sys
import uuid
from datetime import datetime
import random
sys.path.append('gen-py')
import cProfile, pstats
import pyshark
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
#from contact import ContactSvc, ttypes
from mult import MultiplicationService, ttypes
from pyinstrument import Profiler
from pyinstrument.renderers import ConsoleRenderer
	
socket = TSocket.TSocket('localhost', 9090)
transport = TTransport.TFramedTransport(socket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = MultiplicationService.Client(protocol)

transport.open()

def main():
	print(sys.argv[1])
	times = int(sys.argv[1])
	payload = '*'*times
	profiler = Profiler()
	profiler.start()
	result = client.multiply(payload)
	session = profiler.stop()
	print(ConsoleRenderer(unicode=True, color=False, show_all=True).render(session))
	print("Payload size:", len(payload))
	print(result)


if __name__ == '__main__':
	
	#profiler = cProfile.Profile()
	#profiler.enable()
	main()
	#profiler.disable()
	#stats = pstats.Stats(profiler).sort_stats('cumtime')
	#stats.print_stats()
