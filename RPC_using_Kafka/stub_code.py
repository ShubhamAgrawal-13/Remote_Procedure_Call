#!/usr/bin/python3


from time import sleep
from json import dumps
from kafka import KafkaProducer
from kafka import KafkaConsumer
from json import loads
import math

producer = KafkaProducer(  bootstrap_servers=['localhost:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))

consumer = KafkaConsumer('c5',bootstrap_servers=['localhost:9092'],auto_commit_interval_ms=10,auto_offset_reset='earliest',enable_auto_commit=True,group_id='c5',value_deserializer=lambda x: loads(x.decode('utf-8')))

def consume(topic):
	for message in consumer:
		message = message.value
		consumer.commit()
		return message

def sum_rpc ( arg1 , arg2 ) : 
	msg='sum_rpc'+';'+str(arg1)+';'+str(arg2)
	producer.send('s5',value=msg)
	srt=consume('c5')
	return srt



def multiply_rpc ( arg1 , arg2 ) : 
	msg='multiply_rpc'+';'+str(arg1)+';'+str(arg2)
	producer.send('s5',value=msg)
	srt=consume('c5')
	return srt



def max3_rpc ( arg1 , arg2 , arg3 ) : 
	msg='max3_rpc'+';'+str(arg1)+';'+str(arg2)+';'+str(arg3)
	producer.send('s5',value=msg)
	srt=consume('c5')
	return srt



def sqrt_rpc ( arg1 ) : 
	msg='sqrt_rpc'+';'+str(arg1)
	producer.send('s5',value=msg)
	srt=consume('c5')
	return srt



