#!/usr/bin/python3


import requests

url='http://localhost:8080/ServerRPC'

def sum ( arg1 , arg2 ) : 
	PARAMS={'sum':[arg1,arg2] }
	r = requests.get(url = url, params = PARAMS)
	return float(r.text)



def multiply ( arg1 , arg2 ) : 
	PARAMS={'multiply':[arg1,arg2] }
	r = requests.get(url = url, params = PARAMS)
	return float(r.text)



def max3 ( arg1 , arg2 , arg3 ) : 
	PARAMS={'max3':[arg1,arg2,arg3] }
	r = requests.get(url = url, params = PARAMS)
	return float(r.text)



def sqrt ( arg1 ) : 
	PARAMS={'sqrt':[arg1] }
	r = requests.get(url = url, params = PARAMS)
	return float(r.text)



