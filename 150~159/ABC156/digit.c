
#include<stdio.h>

int calc_digit(int n, int k){
    int cnt = 0;
    while(n != 0){
        cnt ++;
        n /= k;
    }
    return cnt;
}

int main(void){
    int n, k;
    scanf("%d""%d", &n, &k);
    printf("%d\n", calc_digit(n, k));
    return 0;
}