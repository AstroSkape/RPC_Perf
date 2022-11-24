package main

import (
	"context"
	"flag"
	"fmt"
	"log"
	"net"
	"strconv"
	"strings"
	

	pb "grpc-docker-async/calc"

	"google.golang.org/grpc"
)

var (
	port = flag.Int("port", 50051, "The server port")
)

type server struct {
	pb.UnimplementedCalculatorServer
}

func decode(s string) [][]int {
	rows := strings.Split(s, ";");
	numRows := len(rows);
	numRows--;
	numCols := len(strings.Split(rows[0], ","));
	arr := make([][]int, numRows);
	for i := 0; i<numRows; i++ {
		arr[i] = make([]int, numCols);
	}
	m := 0;
	n := 0;
	for i := 0; i<numRows; i++ {
		row := rows[i];
		eles := strings.Split(row, ",");
		for j := 0; j<numCols; j++ {
			//fmt.Println("ELE = ", eles[j]);
			arr[m][n], _ = strconv.Atoi(eles[j]);
			n++;
		}
		n = 0;
		m++;
	}
	
	return arr;
}

func encode(arr [][]int, m int, n int) string {
	res := "";
	for i := 0; i<m; i++ {
		for j := 0; j<n; j++ {
			res = res + strconv.Itoa(arr[i][j]);
			if(j == n-1) {
				res = res + ";";
			} else {
				res = res + ",";
			}
		}
	}
	
	return res;
	
}

func (s *server) Multiply(ctx context.Context, in *pb.CalcRequest) (*pb.CalcReply, error) {
	fmt.Print("In Multiply...\n")
	M1 := decode(in.Mat1);
	M2 := decode(in.Mat2);
	m1 := in.M1
	_ = in.M2
	n1 := in.N1
	n2 := in.N2
	
	arr := make([][]int, int(m1));
	for i := 0; i<int(m1); i++ {
		arr[i] = make([]int, int(n2));
	}
	
	for i:=0; i<int(m1); i++ {
		for j := 0; j<int(n2); j++ {
			arr[i][j] = 0;
			for k := 0; k<int(n1); k++ {
				arr[i][j] += (M1[i][k]*M2[k][j]);
			}
		}
	}
	
	return &pb.CalcReply{Value: encode(arr, int(m1), int(n2))}, nil
}

func main() {
	flag.Parse()
	lis, err := net.Listen("tcp", fmt.Sprintf(":%d", *port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterCalculatorServer(s, &server{})
	log.Printf("server listening at %v", lis.Addr())
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
