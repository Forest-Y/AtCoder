
#include<stdio.h>
#include<math.h>

int main(void){
    long int n, dis = 0, min;
    scanf("%ld", &n);
    min = n + 1;
    for(long int i = 1; i <= sqrt(n); i++){
        if(n % i == 0){
            if(i + n / i - 2 < min){
                min = i + n / i - 2;
            }
        }
    }
    printf("%ld\n", min);
    return 0;
}