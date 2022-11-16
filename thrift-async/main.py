import asyncio
import aiothrift

mult_thrift = aiothrift.load('mult.thrift', module_name='mult_thrift')

class Dispatcher:
    def encode(self, arr, m, n):
        s = ""
        for i in range(m):
            for j in range(n):
                s = s + str(arr[i][j])
                if(j == n-1):
                    s = s + ";"
                else:
                    s = s + ","
        return s

    def decode(self, s):
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
    
    async def multiply(self, A, B, m1, n1, m2, n2):
        M1 = self.decode(A)
        M2 = self.decode(B)
        
        await asyncio.sleep(0.001)

        arr = [[sum(a * b for a, b in zip(A_row, B_col))
                        for B_col in zip(*M2)]
                                for A_row in M1]

        return self.encode(arr, int(m1), int(n2))

async def main():
  server = await aiothrift.create_server(mult_thrift.MultiplicationService, Dispatcher())
  async with server:
      await server.serve_forever()

asyncio.run(main())