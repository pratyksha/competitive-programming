#include <stdio.h>
#include <stdlib.h>
int main(void) {
    long long n,k;
	int count=0,i=0;
	scanf("%lld%lld",&n,&k);
	for(i=0;i<n;i++)
	{
	    long long p;
	    scanf("%lld",&p);
	    if(p%k==0)
	    count++;
	}
	printf("%d",count);
	return 0;
}
