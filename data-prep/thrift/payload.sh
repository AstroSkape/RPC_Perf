#!/bin/usr/env bash

echo ""  > thrift.txt
for n in {10..1000..100}; 
do
	python sniffer.py > thrift_$n.txt &
	python client.py $n
	sleep 2
	echo "-----------------------------------"  >> thrift.txt
done
