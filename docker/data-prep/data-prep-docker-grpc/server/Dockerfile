FROM ubuntu:18.04

COPY . /server

WORKDIR /server

RUN apt-get update \
    && apt-get install wget -y \
    && apt install -y protobuf-compiler \
    && apt install golang-goprotobuf-dev -y

RUN wget https://go.dev/dl/go1.19.3.linux-amd64.tar.gz
RUN tar -C /usr/local -xzf go1.19.3.linux-amd64.tar.gz 
ENV PATH $PATH:/usr/local/go/bin

RUN go mod tidy

EXPOSE 50051

CMD [ "go", "run", "main.go" ]