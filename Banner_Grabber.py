#!/usr/bin/python
import socket
import sys
import os


def grab_banner(ip_address, port):
    try:
        s = socket.socket()
        s.connect((ip_address, port))
	print ("11")
        banner = s.recv(1024)
        print
        ip_address + ':' + banner
    except:
        print str(port) + ":" + "is closed"
	print ("12")
        return
	

def all_ports(ips):
	portList = [21, 22, 25, 80, 110, 443]
	for x in range(0, 255):
		for port in portList:
			ip_address = ips + str(x)
			print ip_address
			#ip_address = '192.168.0.' + str(x)
			grab_banner(ip_address, port)


def single_bunner(ip_address):
    portList = [21, 22, 25, 80, 110, 443]
    for port in portList:
        grab_banner(ip_address, port)
    # twenty_bunner()


ips = raw_input("give me ip range without the last 8 bits: ")
all_ports(ips)









