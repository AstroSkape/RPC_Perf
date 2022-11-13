import logging

import grpc
import mult_pb2
import mult_pb2_grpc

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
def gen_random(m1, n1, m2, n2):
	M1 = []
	for i in range(m1):
		M1.append([])
		for j in range(n1):
			M1[i].append(random.randint(1,99))	

	M2 = []
	for i in range(m2):
		M2.append([])
		for j in range(n2):
			M2[i].append(random.randint(1,99))
			
	return M1, M2
	
def run():
    print("Connecting ...")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = mult_pb2_grpc.CalculatorStub(channel)
        m1 = 5
        n1 = 3
        m2 = 3
        n2 = 3
        M1, M2 = gen_random(m1, n1, m2, n2)
        response = stub.Multiply(mult_pb2.CalcRequest(Mat1=encode(M1, m1, n1), Mat2=encode(M2, m2, n2), m1=m1, n1=n1, m2=m2, n2=n2))
    print("Value received: ", decode(response.value))


if __name__ == '__main__':
    logging.basicConfig()
    run()
