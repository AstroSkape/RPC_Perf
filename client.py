import sys
import uuid
from datetime import datetime
sys.path.append('gen-py')

from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
#from contact import ContactSvc, ttypes
from mult import MultiplicationService, ttypes

socket = TSocket.TSocket('localhost', 9090)
transport = TTransport.TFramedTransport(socket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = MultiplicationService.Client(protocol)

transport.open()

result = client.multiply(10,2)

print(result)

