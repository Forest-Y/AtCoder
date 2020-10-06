
#include<stdio.h>

long int fanction(long int n){
    long int cnt = 0;
    if(n < 2){
        return 0;
    }else{
        if(n % 5 == 0){
            cnt = n / 10;
        }
        return cnt + fanction(n - 2);
    }
}

long long int calc(long int n){
    if(n < 2){
        return 1;

    }else{
        return n * calc(n - 2);
    }
}

int main(void){
    long int n;
    scanf("%ld", &n);
    printf("%lld\n", calc(n));
    if(n % 2 == 1){
        printf("%d\n", 0);
        return 0;
    }
    printf("%ld\n", fanction(n));

    return 0;
}