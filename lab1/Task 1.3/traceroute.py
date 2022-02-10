#!/usr/bin/python3

from scapy.all import *
from time import time
import sys
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


args = sys = sys.argv

if len(args) != 2:
    print('Usage:\npython3 traceroute.py <host>')
    exit()

MAX_TTL = 30
host = args[1]
ip = socket.gethostbyname(host)
print(f'traceroute to {host} ({ip}), {MAX_TTL} hops max')

a = IP()
a.dst = ip
a.ttl = 1
b = ICMP()

init_time = int(time() * 1000)
while a.ttl <= MAX_TTL:
    reply = sr1(a/b, verbose=0, timeout=2)
    if reply is not None:
        rep = reply.src
        diff = (int(time() * 1000) - init_time) / a.ttl
        print(f'{str(a.ttl)} {rep} {diff} ms')
        if rep == ip:
            break
    else:
        print(f'{str(a.ttl)} * * *')
    a.ttl += 1


