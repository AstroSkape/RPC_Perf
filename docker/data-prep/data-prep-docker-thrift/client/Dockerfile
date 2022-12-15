FROM alpine

USER root
RUN mkdir /root/tshark
RUN apk --update --no-cache add tshark
RUN apk add bash
RUN apk add python3 py-pip

ENV THRIFT_VERSION v0.17.0

COPY . /client

WORKDIR /client

RUN pip install thrift pyinstrument pyshark

RUN sed -i 's/\r//' payload.sh

RUN chmod +x /usr/bin/dumpcap

CMD [ "bash", "./payload.sh" ]