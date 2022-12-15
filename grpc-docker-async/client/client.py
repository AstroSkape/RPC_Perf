import logging
import asyncio
import random
import grpc
import mult_pb2
import mult_pb2_grpc
from timeit import default_timer as timer

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

def gen_load(step):
	m2 = 5
	n2 = n1 = 5
	m1 = 0
	while True:
		if m1 == 49940:
			break
		m1 += step
		M1 = []
		for i in range(m1):
			M1.append([])
			for j in range(n1):
				M1[i].append(random.randint(10,99))
	
		M2 = []
		for i in range(m2):
			M2.append([])
			for j in range(n2):
				M2[i].append(random.randint(10,99))
		
		yield m1, n1, m2, n2, encode(M1, m1, n1), encode(M2, m2, n2)

def test_case(m1, m2, n1, n2):
	M1 = []
	for i in range(m1):
		M1.append([])
		for j in range(n1):
			M1[i].append(random.randint(10,99))

	M2 = []
	for i in range(m2):
		M2.append([])
		for j in range(n2):
			M2[i].append(random.randint(10,99))
	
	return encode(M1, m1, n1), encode(M2, m2, n2)


	
def run():
	print("Connecting ...")
	channel =  grpc.aio.insecure_channel('172.17.0.2:50051')
	stub = mult_pb2_grpc.CalculatorStub(channel)
	for m1, n1, m2, n2, s1, s2 in gen_load(10):	
		start = timer()
		response = stub.Multiply(mult_pb2.CalcRequest(Mat1=s1, Mat2=s2, m1=m1, n1=n1, m2=m2, n2=n2))
		end = timer()
		delta = (end - start)
		print(m1, delta, len(s1)+len(s2)+4*4)
		#print("Value received: ", decode(response.value))
	#s1, s2 = test_case(49940, 5, 5, 5)
	#response = stub.Multiply(mult_pb2.CalcRequest(Mat1=s1, Mat2=s2, m1=49940, n1=5, m2=5, n2=5))


if __name__ == '__main__':
    logging.basicConfig()
    run()
