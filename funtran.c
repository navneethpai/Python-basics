#include<stdio.h>
void prin(int a[][100],int b[][100],int r,int c)
{
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{
			a[i][j]+=b[i][j];			
			printf("%d  ",a[i][j]);
		}
		printf("\n");
	}
}
void main()
{
	int a[100][100],b[100][100],r,c;
	printf("Enter the row and column:");
	scanf("%d%d",&r,&c);
	printf("Enter the elements of the 2d array\n");	
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{
			scanf("%d",&a[i][j]);
		}
	}
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{
			scanf("%d",&b[i][j]);
		}
	}
	prin(a,b,r,c);
}
