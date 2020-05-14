#!/usr/bin/python3
from stub_code import *
from stub_code import *

inp1=input("Enter number 1 : ")
inp2=input("Enter number 2 : ")
inp3=input("Enter number 3 : ")

print(sum(inp1,inp2))

print(multiply(inp1,inp2))

print(max3(inp1,inp2,inp3))

print(sqrt(inp1))

# import requests

# url="http://localhost:8080/ServerRPC"

# def sum(a,b):
# 	PARAMS = {'sum':[a,b]} 
# 	r = requests.get(url = url, params = PARAMS)
# 	print("result : ",r.text)
# 	return int(r.text)
