#!/usr/bin/python3

import socket
import math

def sum_rpc(a,b):
	return a+b

def multiply_rpc(a,b):
	return a*b

def max3_rpc(a,b,c):
	if(a>b):
		if(a>c):
			return a
		else:
			return c
	else:
		if(b>c):
			return b
		else:
			return c

def sqrt_rpc(a):
	return math.sqrt(a)

s=socket.socket()

port=9923

if(s.bind(('',port))):
	print("Bind unsuccessful : port already in use")

s.listen(5)

print("listening")

while True:
	con,addr=s.accept()
	print("Got Connection from ",addr)
	msg=con.recv(1024).decode('utf-8')
	items=msg.split(';')
	print(items)
	if(items[0]=='sum_rpc'):
		output=sum_rpc(int(items[1]),int(items[2]))
		con.send(bytes(str(output),'utf8'))
	elif(items[0]=='multiply_rpc'):
		output=multiply_rpc(int(items[1]),int(items[2]))
		con.send(bytes(str(output),'utf8'))
	elif(items[0]=='max3_rpc'):
		output=max3_rpc(int(items[1]),int(items[2]),int(items[3]))
		con.send(bytes(str(output),'utf8'))
	elif(items[0]=='sqrt_rpc'):
		output=sqrt_rpc(int(items[1]))
		con.send(bytes(str(output),'utf8'))
	else:
		con.send(bytes(str(-1),'utf8'))
	print(con.recv(1024).decode('utf-8'))
	con.close()
