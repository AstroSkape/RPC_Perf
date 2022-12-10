#!/bin/usr/env bash

echo ""  > thrift.txt
for n in {10..1000..100}; 
do
	python client.py $n > profile_$n.txt
	sleep 2
	echo "-----------------------------------"  >> thrift.txt
done

while true;
do
	echo "" > /dev/null;
done