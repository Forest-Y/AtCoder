
#include<stdio.h>

int main(void){
    int n;
    scanf("%d", &n);
    double odd = 0;
    for(int i = 1; i <= n; i++){
        if(i % 2 == 1){
            odd ++;
        }
    }
    printf("%lf\n", odd / n);
    return 0;

}