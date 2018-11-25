plane={1:'Delhi to kochi at 21hr'}
print 'Welcome to air ways\nHitting return will display the plae schedule'
raw_input()
print plane
seat=['wseat','oseat']
seat1=[0,0]
tseat1=0
tseat2=0
seat2=[0,0]
x=0
ch='y'
while(ch=='y'):
	if tseat1<100:
		print 'occupied seats are(max:50 in each):'
		for i in range(2):
			print seat[i],'=',seat1[i]
		print 'which seat do you prefer\n'
		t=input('Enter seat code(0,1):')
		m=input('Enter no of seats:')
		seat1[t]+=m
		tseat1+=m
		if t==0:
			print 'price=',m*10
		elif t==1:
			print 'price=',m*7
		else:
			print 'No such seats'
	else:	
		print 'all seat are occpuied'
	ch=raw_input('next user(y):')














