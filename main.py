import os,base64_detect,scan,line_scan
dirx = raw_input("Scan Dir :")
listx = scan.scan(dirx) #PHP List
for filename in listx:
	line_scan.line_scan(filename)
	
	
