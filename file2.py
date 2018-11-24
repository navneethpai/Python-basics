n=raw_input('Enter the str:')
try:
	f=open('tx.txt','w')
	f.write(n)
except IOError:
	print 'Fails'
f.close()
f=open('tx.txt','r')
for i in f.read():
	if i==' ':
		print '-',
	else:
		print i,	
