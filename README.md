# SSP_Project

Server coded in golang, client in python

### Run the following to run thrift:

```
go mod tidy
cd thrift
go run main.go -> to run server 
python client.py -> to run client
```

### Run the following to run grpc:

```
cd grpc 
python -m grpc_tools.protoc --proto_path=. ./mult.proto --python_out=./client --grpc_python_out=./client 
protoc --go_out=plugins=grpc:calc mult.proto 
```