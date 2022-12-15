import pyshark

capture = pyshark.LiveCapture(interface='Loopback')

i = 0
sum_ = 0
for packet in capture.sniff_continuously():
	#print(packet.length)
	#if(packet.tcp.srcport == "9090" or packet.tcp.dstport == "9090"):
	if(packet.tcp.srcport == "50051" or packet.tcp.dstport == "50051"):
		sum_ += int(packet.length)
		i += 1
		print(i, ":", packet.length)
		print(i, ":", sum_)
