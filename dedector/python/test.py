import re
mylist = ["dog-asds", "cat-sad", "wtest-sasdsa"]
newlist = []
for i in mylist:
	new,new2 = re.split('-' , i)
	newlist.append(new2)

print newlist
