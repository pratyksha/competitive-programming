#include <stdio.h>
int a[100000];
int main(void) {
	int T=0,N=0,i=0;
	scanf("%d",&T);
	for(i=0;i<T;i++)
	{ 
	  int j=1,minInd=1,p=0;   
	    scanf("%d",&N);
	    for(j=1;j<=N;j++)
	    {
	      scanf("%d",&a[j]);
	    }
	    p=a[1];
	    for(j=1;j<=N;j++)
	    {
	        if(a[j]<p)
	        {
	        p=a[j];
	        minInd=j;
	        }
	    }
	printf("%d\n",minInd);
	}
	return 0;
}
