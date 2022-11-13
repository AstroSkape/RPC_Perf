package main

import (
	"SSP_Project/thrift2/gen-go/tutorial"
	"SSP_Project/thrift2/handler"
	"flag"
	"log"

	"github.com/apache/thrift/lib/go/thrift"
)

func RunServer(transportFactory thrift.TTransportFactory, protocolFactory thrift.TProtocolFactory, addr string, secure bool) error {
	transport, err := thrift.NewTServerSocket(addr)
	if err != nil {
		return err
	}

	handler := handler.NewHandler()
	processor := tutorial.NewMultiplicationServiceProcessor(handler)
	server := thrift.NewTSimpleServer4(processor, transport, transportFactory, protocolFactory)

	log.Printf("Starting simple thrift server on: %s\n", addr)
	return server.Serve()
}

var (
	addr = flag.String("addr", "localhost:9090", "Thrift Address to listen on")
)

func main() {
	flag.Parse()

	transportFactory := thrift.NewTFramedTransportFactory(thrift.NewTTransportFactory())
	protocolFactory := thrift.NewTBinaryProtocolFactoryDefault()

	if err := RunServer(transportFactory, protocolFactory, *addr, false); err != nil {
		log.Println("error running thrift server: ", err)
	}
}
