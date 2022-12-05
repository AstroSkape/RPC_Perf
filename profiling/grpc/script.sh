#!/bin/bash
for (( c=40; c<=4000000; c*=10 ))
do
    sum1=0.0
    sum2=0.0
    sum3=0.0
    for i in {1..10}
    do
        #python client/client.py $c
        var=`python client/client.py $c`
        var1=`echo $var | awk -F ' ' '{print $1}'`
        var2=`echo $var | awk -F ' ' '{print $2}'`
        var3=`echo $var | awk -F ' ' '{print $3}'`
        sum1=$(echo "$sum1 + $var1" | bc)
        sum2=$(echo "$sum2 + $var2" | bc)
        sum3=$(echo "$sum3 + $var3" | bc)
        #echo "$var1 $var2 $var3"
    done
    sum1=$(echo "$sum1 / 10" | bc -l)
    sum2=$(echo "$sum2 / 10" | bc -l)
    sum3=$(echo "$sum3 / 10" | bc -l)
    echo "$c $sum1 $sum2 $sum3"
done

