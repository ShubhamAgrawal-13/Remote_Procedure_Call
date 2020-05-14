#!/usr/bin/python3


from time import sleep
from json import dumps
from kafka import KafkaProducer
from kafka import KafkaConsumer
from json import loads
import math

producer=''
#consumer=''

def initialize():
	global producer
	global consumer
	producer=KafkaProducer(  bootstrap_servers=['localhost:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))
	consumer = KafkaConsumer('ckl',bootstrap_servers=['localhost:9092'],auto_offset_reset='latest',group_id='mg',value_deserializer=lambda x: loads(x.decode('utf-8')))


def produce(topic,msg):
	global producer
	global consumer
	print('Sent message to '+msg)
	producer.send(topic, value=msg)

def consume(topic):
	print("ttt")
	for message in consumer:
		message = message.value
		print(message,' ---s ')
		return message

def sum_rpc ( arg1 , arg2 ) : 
	msg='sum_rpc'+';'+str(arg1)+';'+str(arg2)
	produce('skl',msg)
	srt=consume('ckl')
	return srt

def multiply_rpc ( arg1 , arg2 ) : 
	msg='multiply_rpc'+';'+str(arg1)+';'+str(arg2)
	produce('skl',msg)
	srt=consume('ckl')
	return srt

def max3_rpc ( arg1 , arg2 , arg3 ) : 
	msg='max3_rpc'+';'+str(arg1)+';'+str(arg2)+';'+str(arg3)
	produce('skl',msg)
	srt=consume('ckl')
	return srt



def sqrt_rpc ( arg1 ) : 
	msg='sqrt_rpc'+';'+str(arg1)
	produce('skl',msg)
	srt=consume('ckl')
	return srt



