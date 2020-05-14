#!/usr/bin/python3

import socket

# try:
# 	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# except:
# 	print("Couldn't Able to create a socket")

# s.connect(('',9923))

port=9923

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

stub_code.write("import socket\n\n")

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

	stub_code.write("\ts=socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n")
	stub_code.write("\ts.connect(('',{}))\n".format(port))
	stub_code.write("\tmsg={}\n".format(msg))
	stub_code.write("\ts.send(bytes(str(msg),'utf8'))\n")
	stub_code.write("\tsrt=s.recv(1024).decode('utf-8')\n")
	stub_code.write("\ts.send(b'Output Received')\n")
	stub_code.write("\ts.close()\n")
	stub_code.write("\treturn srt\n")
	stub_code.write("\n\n\n")

stub_code.close()
