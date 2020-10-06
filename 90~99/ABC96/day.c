#include<stdio.h>

int main(void){
    int a, b, cnt;
    scanf("%d""%d", &a, &b);
    if(a <= b){
        cnt = a;
    }else{
        cnt = a - 1;
    }
    printf("%d\n", cnt);
}