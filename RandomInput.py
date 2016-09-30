from random import randint

size=100000000;
i=0;
randomlist=[]

while i<size-1:
	randomlist.append(randint(-size,size));
	i+=1;
	
fout = open('/Users/vinaykumar/Documents/py/input10pow7.txt','w');
print >>fout, randomlist;
fout.close();
