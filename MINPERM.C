#include <stdio.h>

int main(void) {
	int T=0,n=0,i,j;
	scanf("%d",&T);
	for(i=0;i<T;i++)
	{
	    scanf("%d",&n);
	    int a[n];
	    for(j=0;j<n;j++)
	    a[j]=j+1;
	    for(j=0;j<n;j=j+2)
	    {
	        if(n%2==0||j!=(n-3))
	        printf("%d %d ",a[j+1],a[j]);
	        else
	        {
	        printf("%d %d %d ",a[j+1],a[j+2],a[j]);
	        break;
	            
	        }
	    }
	    printf("\n");
	}
	return 0;
}

