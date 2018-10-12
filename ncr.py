def fac(n):
	fac=1
	for i in range(n,1,-1):
		fac*=i	
	return fac
n=input("Enter the vale of n:")
r=input("Enter the vale of r:")
nf=fac(n)
rf=fac(r)
n_r=fac(n-r)
a=n_r*rf
b=nf/a
print b
