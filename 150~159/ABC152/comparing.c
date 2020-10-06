
#include<stdio.h>
#include<string.h>

int main(void){
    int a, b, cnt, x;
    scanf("%d""%d", &a, &b);
    if(a < b){
        cnt = b;
        x = a;
    }else{
        cnt = a;
        x = b;
    }
    for(int i = 0; i < cnt; i++){
        printf("%d", x);
    }
    printf("\n");
    return 0;
}