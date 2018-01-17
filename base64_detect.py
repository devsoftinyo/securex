import os,base64,re

def detect(text):
	x = re.findall('(".*")',text)
	return x

def decode(text):
	decoded = base64.b64decode(text)
	return decoded

def main(text):
	decodeds = []
	dete = detect(text)
	for i in dete:
		decoded = decode(i)
		decodeds.append(decoded)
	return decodeds
