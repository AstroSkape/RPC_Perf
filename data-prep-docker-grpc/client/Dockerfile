FROM python:3.9

RUN pip install grpcio-tools pyshark pyinstrument

COPY . .

CMD [ "python3", "client.py", "1000" ]