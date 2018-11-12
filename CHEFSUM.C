#include <stdio.h>
int a[100000];
int main(void) {
	int T=0,N=0,i=0;
	scanf("%d",&T); //number of test cases
	for(i=0;i<T;i++)
	{ 
	  int j=1,minInd=1,p=0;   
	    scanf("%d",&N); // number of elements in array A
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
	printf("%d\n",minInd); // minimized sum of prefix sum and suffix sum
	}
	return 0;
}
