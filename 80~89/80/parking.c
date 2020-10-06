
#include<stdio.h>

int main(void){
    int a, b, t;
    scanf("%d""%d""%d", &t, &a, &b);
    if(a * t > b){
        printf("%d\n", b);
    }else{
        printf("%d\n", a * t);
    }
    return 0;
}