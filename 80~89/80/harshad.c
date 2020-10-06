
#include<stdio.h>

int main(void){
    int x, sum = 0, y;
    scanf("%d", &x);
    y = x;
    while(y >= 1){
        sum += y % 10;
        y /= 10;
    }
    if(x % sum == 0){
        printf("Yes\n");
    }else{
        printf("No\n");
    }
    return 0;
}