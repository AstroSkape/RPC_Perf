import pyshark

capture = pyshark.LiveCapture(interface='eth0')

i = 0
sum_ = 0

for packet in capture.sniff_continuously():
	#print(packet.length)
	#if(packet.tcp.srcport == "9090" or packet.tcp.dstport == "9090"):
    print(packet)
    '''if(packet.tcp.srcport == "50051" or packet.tcp.dstport == "50051"):
            sum_ += int(packet.length)
            i += 1
            #print(i, ":", packet.length)
            #print(i, ":", sum_)
            print(packet)'''