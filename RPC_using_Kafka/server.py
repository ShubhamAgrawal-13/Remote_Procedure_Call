#!/usr/bin/python3

from time import sleep
from json import dumps
from kafka import KafkaProducer
from kafka import KafkaConsumer
from json import loads
from colorama import Fore
import math

server=input("Enter server id : ")
client=input("Enter client id : ")

producer=KafkaProducer(  bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8')
                      )

consumer = KafkaConsumer(
							    server,
								bootstrap_servers=['localhost:9092'],
								auto_offset_reset='latest',
								value_deserializer=lambda x: loads(x.decode('utf-8'))
						)


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
	
#server side code
for message in consumer:
	msg = message.value
	msg=str(msg)
	print(msg,'-------')
	items=msg.split(';')
	print(items)
	if(items[0]=='sum_rpc'):
		output=sum_rpc(int(items[1]),int(items[2]))
		output=str(output)
		producer.send(client,output)
	elif(items[0]=='multiply_rpc'):
		output=multiply_rpc(int(items[1]),int(items[2]))
		output=str(output)
		producer.send(client,output)
	elif(items[0]=='max3_rpc'):
		output=max3_rpc(int(items[1]),int(items[2]),int(items[3]))
		output=str(output)
		producer.send(client,output)
	elif(items[0]=='sqrt_rpc'):
		output=sqrt_rpc(int(items[1]))
		output=str(output)
		producer.send(client,output)
	else:
		producer.send(client,"-1")

# frombeginning


# 1 2 3 4 5 


# c 		st 
# c1 ---> [mygroup] --> mygroup--->offset--->partition
# c2 ----> [default] -->>x random
# 0 1 2 3 4 5 6 7 ()