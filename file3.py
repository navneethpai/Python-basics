n=raw_input('Enter the str:')
m=[]
f=open('pal.txt','w')
f.write(n)
f.close()
f=open('pal.txt','r')	
for i in f:
	m.append(i)
for i in f:
	m.append(i)
print len(m)
for j in range(len(m)):	
	for k in f.read():	
		if k=='':		
			continue
		else:
			for i in m:
				if i==i[::-1]:
					print i,'Its paladrone\n'
				else:
					print i,'its not\n'
f.close()
