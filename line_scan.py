import os
f = open("wordlist.txt")
lookup = f.readlines()
lookup = list(map(lambda x:x.strip(),lookup)) # Clean \n
i = []
print lookup
filename = "test.php"
with open(filename) as myFile:
    for num, line in enumerate(myFile, 1):
		for i in lookup:
		    if i in line:
		        print '[+] Found',i,' in (',num,')'
