
#include<stdio.h>

int main(void){
    int a, b, c;
    scanf("%d""%d""%d", &a, &b, &c);
    if((a == b && b != c) || (a == c && a != b) || (b == c && b != a)){
        printf("Yes\n");
        return 0;
    }else{
        printf("No\n");
        return 0;
    }
}