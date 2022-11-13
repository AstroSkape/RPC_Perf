import sys
import uuid
from datetime import datetime
import random
sys.path.append('gen-py')

from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
#from contact import ContactSvc, ttypes
from mult import MultiplicationService, ttypes

def encode(arr, m, n):
	s = ""
	for i in range(m):
		for j in range(n):
			s = s + str(arr[i][j])
			if(j == n-1):
				s = s + ";"
			else:
				s = s + ","
	return s

def decode(s):
	rows = s.split(";")
	numRows = len(rows)
	numRows-=1
	numCols = len(rows[0].split(","))
	arr = []
	m = 0
	n = 0
	for i in range(numRows):
		row = rows[i]
		eles = row.split(",")
		arr.append([])
		for j in range(numCols):
			arr[m].append(int(eles[j]))
			n+=1
		n = 0
		m+=1
	return arr
	
socket = TSocket.TSocket('localhost', 9090)
transport = TTransport.TFramedTransport(socket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = MultiplicationService.Client(protocol)

transport.open()

m1 = 5
n1 = 3
M1 = []
for i in range(m1):
	M1.append([])
	for j in range(n1):
		M1[i].append(random.randint(1,99))	

m2 = 3
n2 = 3
M2 = []
for i in range(m2):
	M2.append([])
	for j in range(n2):
		M2[i].append(random.randint(1,99))
		
result = client.multiply(encode(M1, m1, n1), encode(M2, m2, n2), m1, n1, m2, n2)

print(decode(result))

