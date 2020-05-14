#!/usr/bin/python3

import requests

url="http://localhost:8080/ServerRPC"
PARAMS = {'method':1} 
r = requests.get(url = url, params = PARAMS)
# print(r.text)
file=r.text.split(':')
list_of_methods=[]

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


for line in file:
	list_of_methods.append(line.split())
# print(list_of_methods)
stub_code=open('stub_code.py','w+')

stub_code.write("#!/usr/bin/python3\n\n\n")

stub_code.write("import requests\n\n")
stub_code.write("url='http://localhost:8080/ServerRPC'\n\n")

for method in list_of_methods:
	if(method==[]):
		continue
	stub_code.write("def {} ( ".format(method[0]))
	num=int(method[1])
	msg="PARAMS={"
	msg+="'{}'".format(str(method[0]))+":[";
	if(num==0):
		stub_code.write(") : \n")
		msg+="]"
	else:
		for i in range(num-1):
			stub_code.write("arg"+str(i+1)+" , ")
			msg+="arg"+str(i+1)+","
		stub_code.write("arg"+str(num)+" ) : \n")
		msg+="arg"+str(num)+"] }"
	stub_code.write("\t{}\n".format(msg))
	stub_code.write("\tr = requests.get(url = url, params = PARAMS)\n")
	stub_code.write("\treturn float(r.text)\n")
	stub_code.write("\n\n\n")

stub_code.close()
