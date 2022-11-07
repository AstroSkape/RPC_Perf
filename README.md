# RPC Performance Comparison 

Server coded in golang, client in python

### Run the following to run thrift:

```
go mod tidy
cd thrift
thrift --gen go mult.thrift 
thrift --gen py mult.thrift 
go run main.go 

source venv/bin/activate
virtualenv venv
source venv/bin/activate
python client.py 
```

### Run the following to run grpc:

```
cd grpc 
python -m grpc_tools.protoc --proto_path=. ./mult.proto --python_out=./client --grpc_python_out=./client 
protoc --go_out=plugins=grpc:calc mult.proto 

go run server/main.go
python client/client.py
```