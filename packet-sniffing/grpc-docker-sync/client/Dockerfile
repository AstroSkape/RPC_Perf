FROM python:3.9

USER root

RUN pip install grpcio-tools

COPY . .

RUN pip install pyshark

RUN apt update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y tshark

CMD ./run.sh