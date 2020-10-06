
#include<stdio.h>

int main(void){
    int n, k, m, x, sum = 0;
    scanf("%d""%d""%d", &n, &k, &m);
    for(int i = 0; i < n - 1; i++){
        scanf("%d", &x);
        sum += x;
    }

    if(m * n - sum >= 0 && m * n - sum <= k){
        printf("%d\n", m * n - sum);
    }else if(m * n - sum <= 0){
        printf("%d\n", 0);
    }else{
        printf("%d\n", -1);
    }
    return 0;
}