#include<stdio.h>
int *test(int a[],int n)
{
	int e=0,o=0;
	static int c[2];
	for(int i=0;i<n;i++)
	{
		if(a[i]%2==0)
			e++;
		else
			o++;
	}
	c[0]=e;
	c[1]=o;
	//printf("%d**%d",c[0],c[1]);
	return c;
}
void main()
{
	int a[100],n,*p;
	scanf("%d",&n);
	for(int i=0;i<n;i++)
		scanf("%d",&a[i]);
	p=test(a,n);
	printf("even=%d\nodd=%d",*p,*p+1);
}
