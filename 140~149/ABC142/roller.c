
#include<stdio.h>

int main(void){
    int n, k, h, cnt = 0;
    scanf("%d""%d", &n, &k);
    for(int i = 0; i < n; i++){
        scanf("%d", &h);
        if(h >= k){
            cnt ++;
        }
    }
    printf("%d\n", cnt);
    return 0;
}