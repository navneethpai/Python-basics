#Program for creating an calculator
def _add(a,b):
	return a+b
def _sub(a,b):
	return a-b
def _multi(a,b):
	return a*b
def _dev(a,b):
	return a/b
def _exp(a):
	return 2.71828**a
for i in range (100):
	print "MENU\n____\n1.Addition\n2.Subtraction\n3.Multiply\n4.Division\n5.Expotinal"
	n=input("Enter the choice:")
	x=0
	if n!=5:
		a=input("Enter the numbers for operations:")
		b=input()	
		if n==1:
			x=_add(a,b)
		elif n==2:
			x=_sub(a,b)
		elif n==3:
			x=_multi(a,b)
		elif n==4:
			x=_dev(a,b)
	else:
	        a=input("Enter the number:")
	        x=_exp(a)
	print x
	ch=raw_input("Do you want to continue?")
	if ch=="no":
		break

