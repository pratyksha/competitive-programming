#include <stdio.h>
#include <string.h>
int main(void) {
    int t,i=0;
	char s[100];
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
	    int j=0,k=0,l=0,c=0,ct=0;
	    scanf("%s",s);
	    l=strlen(s);
	  for(j=0;j<l-1;j++)
	  {
	      for(k=j+1;k<l;k++)
	      {
	          if(s[j]==s[k])
	          c++;
	      }
	      if(c>0)
	      ct++;
	  }
	if(ct>0)
	printf("yes\n");
	else
	printf("no\n");
	}
	return 0;
}
