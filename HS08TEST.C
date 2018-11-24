#include <stdio.h>
#include <stdlib.h>
int main(void) {
    int i=0; 
    float o=0;
    scanf("%d %f",&i,&o); // i = amt of cash to withdraw, o = initial account balance
    if(i%5!=0||(i+0.50)>o)
    printf("%.2f",o); // since balance not enough, print current balance
    else
    printf("%.2f",o-(i+0.50)); // print account balance after the attempted transaction
	return 0;
}
