import os
import shutil
lis=[]
i=1
destinationDir='C:\Users\Prasanth\Desktop\Desktop'
while os.path.exists(destinationDir):
	destinationDir=destinationDir+str(i)
	i+=1
os.makedirs(destinationDir)
lis=os.listdir('C:\Users\Prasanth\Desktop')
print lis
for x in lis:
	if x==__file__:
		continue
	shutil.move(x, destinationDir)
