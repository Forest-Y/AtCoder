
#include<stdio.h>

int main(void){
    int h, a, cnt = 0;
    scanf("%d""%d", &h, &a);
    while(h > 0){
        h -= a;
        cnt ++;
    }
    printf("%d\n", cnt);
    return 0;
}