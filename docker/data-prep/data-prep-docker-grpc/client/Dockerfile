FROM python:3.9

RUN pip install grpcio-tools pyinstrument

COPY . .

CMD [ "bash", "payload.sh" ]