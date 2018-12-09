#include <stdio.h>

int main(void) {
	int T=0,n=0,i,j;
	scanf("%d",&T);
	for(i=0;i<T;i++) // number of test cases
	{
	    scanf("%d",&n); // number of elements of array
	    int a[n];
	    for(j=0;j<n;j++)
	    a[j]=j+1; // storing n distinct elements in the array
	    for(j=0;j<n;j=j+2)
	    {
	        if(n%2==0||j!=(n-3))
	        printf("%d %d ",a[j+1],a[j]); // lexicographically smallest good permutation
	        else
	        {
	        printf("%d %d %d ",a[j+1],a[j+2],a[j]); // lexicographically smallest good permutation
	        break;
	            
	        }
	    }
	    printf("\n");
	}
	return 0;
}

