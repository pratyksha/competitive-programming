#include <stdio.h>
#include <stdlib.h>
int main(void) {
	int t;
	scanf("%d\n",&t);
	while((t--)>0) // number of test cases
	{
	 int p=0,ct=0,i=5;
	 scanf("%d\n",&p);
	 if(p<5)
	 {
	     printf("0\n");
	     continue;
	 }
	 else{
	 for ( i=5; p/i>=1; i *= 5)
          ct += p/i;
	 printf("%d\n",ct);
	}
	}
	return 0;
}
