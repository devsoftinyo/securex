# -*- coding: utf-8 -*-
import os,re
count = 0
desc = []
look = []
f = open("wordlist.txt")
lookup = f.readlines()
lookup = list(map(lambda x:x.strip(),lookup)) 
###############################################
######## For Desc and Wordlist split ##########
for i in lookup: 
	new,new2 = re.split('-' , i)
	look.append(new)
	desc.append(new2)

################################################

i = []

filename = "test.php"
with open(filename) as myFile:
    for num, line in enumerate(myFile, 1):
		for c,i in enumerate(look):
			if i in line:
				print '[+] Dosya içinde ',num,'. satırda "',i,'" kodu bulundu.(',desc[c],''
			
