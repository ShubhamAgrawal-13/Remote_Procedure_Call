#!/usr/bin/python3


import socket

def sum_rpc ( arg1 , arg2 ) : 
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('',9923))
	msg='sum_rpc'+';'+str(arg1)+';'+str(arg2)
	s.send(bytes(str(msg),'utf8'))
	srt=s.recv(1024).decode('utf-8')
	s.send(b'Output Received')
	s.close()
	return srt



def multiply_rpc ( arg1 , arg2 ) : 
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('',9923))
	msg='multiply_rpc'+';'+str(arg1)+';'+str(arg2)
	s.send(bytes(str(msg),'utf8'))
	srt=s.recv(1024).decode('utf-8')
	s.send(b'Output Received')
	s.close()
	return srt



def max3_rpc ( arg1 , arg2 , arg3 ) : 
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('',9923))
	msg='max3_rpc'+';'+str(arg1)+';'+str(arg2)+';'+str(arg3)
	s.send(bytes(str(msg),'utf8'))
	srt=s.recv(1024).decode('utf-8')
	s.send(b'Output Received')
	s.close()
	return srt



def sqrt_rpc ( arg1 ) : 
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('',9923))
	msg='sqrt_rpc'+';'+str(arg1)
	s.send(bytes(str(msg),'utf8'))
	srt=s.recv(1024).decode('utf-8')
	s.send(b'Output Received')
	s.close()
	return srt



