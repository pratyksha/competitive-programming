#include <stdio.h>
#include <stdlib.h>
int main(void) {
    int i=0;
    float o=0;
    scanf("%d %f",&i,&o);
    if(i%5!=0||(i+0.50)>o)
    printf("%.2f",o);
    else
    printf("%.2f",o-(i+0.50));
	return 0;
}
