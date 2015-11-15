#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
author: Michael <onehao333@gmail.com>



"""
def tcp():
    import socket
    target_host = "127.0.0.1"
    target_port = 9999 # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # connect the client
    client.connect((target_host, target_port)) # send some data
    client.send("GET / HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n") # receive some data
    response = client.recv(4096)
    print response
    
def udp():
    import socket
    target_host = "www.baidu.com"
    target_port = 80
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # send some data
    client.sendto("AAABBBCCC",(target_host,target_port))
    # receive some data
    data, addr = client.recvfrom(4096)
    print data

tcp()
print('---------------------------------------------')
udp()