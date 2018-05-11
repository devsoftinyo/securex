import os

def scan(dir):
	listf = []
	root = dir
	path = os.path.join(root, "firstdir")
	for path, subdirs, files in os.walk(root):
	    for name in files:
			filename = os.path.join(path, name)
			extension = os.path.splitext(filename)[1]
			y = os.path.isdir(filename)
			if y == False:
				if extension == ".php":
					listf.append(filename)

	return listf


