n=raw_input('Enter the str:')
try:
	f=open('tx.txt','r+')
	f.write(n)
finally IOError:
	print 'Fails'
for i in f.read():
	if i==' ':
		f.write('-')
f.close()
f=open ("tx.txt",'r') 
for j in f.readlines():
	print j	
f.close()
