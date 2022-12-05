package main

import (
	"context"
	"flag"
	"fmt"
	"log"
	"net"

	pb "SSP_Project/profiling/grpc/calc"

	"google.golang.org/grpc"
)

var (
	port = flag.Int("port", 50051, "The server port")
)

type server struct {
	pb.UnimplementedCalculatorServer
}

func (s *server) Multiply(ctx context.Context, in *pb.CalcRequest) (*pb.CalcReply, error) {
	return &pb.CalcReply{Value: "done"}, nil
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
