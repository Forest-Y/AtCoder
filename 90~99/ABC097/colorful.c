
#include<stdio.h>
#include<stdlib.h>

int main(void){
    int  a, b, c, d;
    scanf("%d""%d""%d""%d", &a, &b, &c, &d);
    if(abs(a - c) <= d|| (abs(a - b) <= d && abs(b - c) <= d)){
        printf("Yes\n");
        return 0;
    }
    printf("No\n");
    return 0;
}