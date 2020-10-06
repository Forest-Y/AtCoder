
#include<stdio.h>

int judge_min(int a, int b){
    if(b < a){
        return b;

    }else{
        return a;
    }
}

int judge_max(int a, int b){
    if(a < b){
        return b;
    }else{
        return a;
    }
}

int main(void){
    int a, b, c, x, y, sum1 = 0, sum2 = 0, sum3 = 0, min;
    scanf("%d""%d""%d""%d""%d", &a, &b, &c, &x, &y);
    sum1 = a * x + b * y;
    min = judge_min(x, y);
    sum2 = c * min * 2 + a * (x - min) + b * (y - min);
    sum3 = c * judge_max(x, y) * 2;
    printf("%d\n", judge_min(sum3, judge_min(sum1, sum2)));
    return 0;
}