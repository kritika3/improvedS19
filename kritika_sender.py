#!/usr/bin/python3

import socket

target_ip="172.31.6.5"
target_port=9999
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    msg=input("Enter your message  :  ")
    n=msg.encode('ascii')
    s.sendto(n,(target_ip,target_port))

