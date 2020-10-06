
#include<stdio.h>

long int calc(long int n, int a, int b){
    long int sum = 1, x = 1, x_a = 1, x_b = 1;
    for(long int i = 1; i <= n / 2; i++){
        x = x / i  * (n - i + 1);
        if(i == a || n - i + 1 == a){
            x_a = (n - i + 1) / i;
        }
        if(i == b || n - i  == b){
            x_b = (n - i + 1) / i;
        }
        /*printf("%ld:%ld\n",i, x % 1000000007);*/
        if(n % 2 == 0 && i != n / 2){
            sum += x % 1000000007;
        }
        sum += x % 1000000007;
    }
    /*printf("%ld %ld\n", x_a, x_b);
    printf("sum:%ld\n", sum);*/
    sum = sum - x_a - x_b;
    return sum;
}
int main(void){
    long int n;
    int  a, b;
    scanf("%ld""%d""%d", &n, &a, &b);
    printf("%ld\n", calc(n, a, b) );
    return 0;
}