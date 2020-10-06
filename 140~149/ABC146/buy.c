
#include<stdio.h>

int calc(long int i){
    int digit = 0;
    while(i >= 1){
        digit ++;
        i /= 10;
    }
    return digit;
}

long int calc_mean(long int a, long int b){
    if((a + b) % 2 == 0){
        return (a + b) / 2;
    }
    return (a + b) / 2 + 1;
}

long int calc_price(long int a, long int b, long int x, long int begin, long int end){
    long int mean = /*(begin + end) / 2; */ calc_mean(begin, end);
    int digit = calc(mean);
    /*printf("digit:%d\n", digit);*/
    /*printf("begin:%ld end:%ld mean:%ld\n", begin, end, mean);*/
    if(a > x || b > x){
        return 0;
    }
    if(x == mean * a + b * digit || begin == end){
        return mean;
    }
    if(x < mean * a + b * digit){
        return calc_price(a, b, x, begin, mean - 1);
    }else if(x > mean * a + b * digit){
        return calc_price(a, b, x, mean, end);
    }
    return 0;
}

int main(void){
    
    long int a, b, x, max = 1000000000;
    scanf("%ld""%ld""%ld", &a, &b, &x);
    if(max < x){
        printf("%ld\n", calc_price(a, b, x, 1, max));
        return 0;
    }
    printf("%ld\n", calc_price(a, b, x, 1, x));
    return 0;
}