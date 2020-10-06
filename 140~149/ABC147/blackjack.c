#include<stdio.h>

int main(void){
    int a, b, c;
    scanf("%d""%d""%d", &a, &b, &c);
    if(a + b + c >= 22){
        printf("bust\n");
        return 0;
    }
    printf("win\n");
    return 0;
}