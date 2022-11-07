# SSP_Project

### Run the following:

```
go mod tidy
cd thrift
go run main.go -> to run server 
python client.py -> to run client
```

```
cd grpc 
python -m grpc_tools.protoc --proto_path=. ./mult.proto --python_out=./client --grpc_python_out=./client 
protoc --go_out=plugins=grpc:calc mult.proto 
```