#!/usr/bin/env python3

from scapy.all import *

def print_pkt(pkt):
    pkt.show()

pkt = sniff(iface='br-3e5f42528ad9', filter='icmp', prn=print_pkt)
