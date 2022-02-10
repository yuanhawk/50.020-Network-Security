#!/usr/bin/python3

from scapy.all import *

def spoof(pkt):
    if ICMP in pkt and pkt[ICMP].type != 8:
        return
    ip = IP(src=pkt[IP].dst, dst=pkt[IP].src, ihl=pkt[IP].ihl)
    icmp = ICMP(type=0, id=pkt[ICMP].id, seq=pkt[ICMP].seq)
    data = pkt[Raw].load
    new_pkt = ip/icmp/data

    send(new_pkt)
    print('Sending spoofed pkt from: ' + pkt[IP].src + " back to " + pkt[IP].dst)

pkt = sniff(filter='icmp', prn=spoof)
