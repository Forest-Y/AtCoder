
#include<stdio.h>

int main(void){
    long int a, b, k;
    scanf("%ld""%ld""%ld", &a, &b, &k);
    if(a < k){
        k -= a;
        a = 0;
        if(b < k){
            printf("%d %d\n", 0, 0);
            return 0;
        }else{
            b -= k;
            printf("%ld %ld\n", a, b);
            return 0;
        }
    }else{
        a -= k;
        printf("%ld %ld\n", a, b);
        return 0;
    }

    printf("%ld %ld\n", a, b);
    return 0;
}