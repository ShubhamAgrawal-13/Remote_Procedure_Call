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

filename=input("Enter file name : ")
f = open(filename, "r")
contents = f.readlines()
f.close()

value="from stub_code import *\n"
contents.insert(1, value)

f = open(filename, "w")
contents = "".join(contents)
f.write(contents)
f.close()

header_file=open('methods_file.txt','r')
file=header_file.readlines()

list_of_methods=[]

for line in file:
	list_of_methods.append(line.split())

stub_code=open('stub_code.py','w+')

stub_code.write("#!/usr/bin/python3\n\n\n")

stub_code.write("from time import sleep\nfrom json import dumps\nfrom kafka import KafkaProducer\nfrom kafka import KafkaConsumer\nfrom json import loads\nimport math\n\n")
stub_code.write("producer = KafkaProducer(  bootstrap_servers=['localhost:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))\n\n")
stub_code.write("consumer = KafkaConsumer('{}',bootstrap_servers=['localhost:9092'],auto_commit_interval_ms=10,auto_offset_reset='earliest',enable_auto_commit=True,group_id='{}',value_deserializer=lambda x: loads(x.decode('utf-8')))\n".format(client,client))

stub_code.write("\ndef consume(topic):\n")
stub_code.write("\tfor message in consumer:\n\t\tmessage = message.value\n\t\tconsumer.commit()\n\t\treturn message\n\n")


for method in list_of_methods:
	stub_code.write("def {} ( ".format(method[0]))
	num=int(method[1])
	msg="'{}'+';'".format(method[0])
	if(num==0):
		stub_code.write(") : \n")
	else:
		for i in range(num-1):
			stub_code.write("arg"+str(i+1)+" , ")
			msg=msg+"+str(arg"+str(i+1)+")+';'"
		stub_code.write("arg"+str(num)+" ) : \n")
		msg=msg+"+str(arg"+str(num)+")"

	# stub_code.write("\tproduce('{}','{}')\n".format(server,client))
	stub_code.write("\tmsg={}\n".format(msg))
	stub_code.write("\tproducer.send('{}',value=msg)\n".format(server))
	stub_code.write("\tsrt=consume('{}')\n".format(client))
	stub_code.write("\treturn srt\n")
	stub_code.write("\n\n\n")


stub_code.close()
