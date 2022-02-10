#!/usr/bin/env python3

from scapy.all import *

def print_pkt(pkt):
    pkt.show()

pkt = sniff(iface='br-3e5f42528ad9', filter='tcp && src host 10.9.0.5 && dst port 23', prn=print_pkt)
