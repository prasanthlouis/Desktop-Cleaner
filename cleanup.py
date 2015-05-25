import os
import shutil
lis=[]
destinationDir='C:\Users\Prasanth\Desktop\Desktop'
if not os.path.exists(destinationDir): 
	os.makedirs(destinationDir)
lis=os.listdir('C:\Users\Prasanth\Desktop')
print lis
for x in lis:
	if x==__file__:
		continue
	shutil.move(x, destinationDir)
