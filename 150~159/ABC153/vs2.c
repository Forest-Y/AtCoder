
#include<stdio.h>

int main(void){
    int h, n, sum = 0, a;
    scanf("%d""%d", &h, &n);
    for(int i = 0; i < n; i++){
        scanf("%d", &a);
        sum += a;
    }
    if(sum < h){
        printf("No\n");
    }else{
        printf("Yes\n");
    }

}