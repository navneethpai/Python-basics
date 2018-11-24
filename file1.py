import pickle
list1=[]
n=input("Enter the total no of elements:")
fo=open('odd.txt','w')
fe=open('even.txt','w')
for i in range(n):
	a=input('Enter the element:')
	if a%2==0:
		list1.append(pickle.dump(a,fe))
	else:
		list1.append(pickle.dump(a,fo))
fe.close()
fo.close()
f1=open('odd.txt','r')
f2=open('even.txt','r')
print'Printing the odd file'
for i in f1.read():
	print i
print 'Printing the even file'
for i in f2.read():
	print i
fe.close()
fo.close()
