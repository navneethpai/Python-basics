def tri(a,b,c):
	x=a**2
	y=(b**2)+(c**2)	
	if(x==y):
		return 1
	else:
		return 0
x=input("Longest side:")
y=input("Height:")
z=input("Base")
a=tri(x,y,z)
print a
