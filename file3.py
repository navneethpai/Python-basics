n=raw_input('Enter the str:')
f=open('pal.txt','r+')
f.truncate(0)
f.write(n)
f.close()
m=[]
f=open('pal.txt','r')	
for i in f:
	m.append(i)
for i in range(len(m)):
	a=m[i]	
	if a==a[::-1]:
		print a,'Its paladrone\n'
		continue
	else:
		print a,'its not\n'
		continue
f.close()
