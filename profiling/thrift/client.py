import sys
import uuid
from datetime import datetime
import random
sys.path.append('gen-py')
import cProfile, pstats

from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
#from contact import ContactSvc, ttypes
from mult import MultiplicationService, ttypes
	
socket = TSocket.TSocket('localhost', 9090)
transport = TTransport.TFramedTransport(socket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = MultiplicationService.Client(protocol)

transport.open()

def main():
	payload = '*'*1000000
	result = client.multiply(payload)
	print("Payload size:", len(payload))
	print(result)


if __name__ == '__main__':
	
	#profiler = cProfile.Profile()
	#profiler.enable()
	main()
	#profiler.disable()
	#stats = pstats.Stats(profiler).sort_stats('cumtime')
	#stats.print_stats()