
#include<stdio.h>

long int max(long int x, long int y){
    if(x < y){
        return y;
    }else{
        return x;
    }
}

int main(void){
    long int c, sum_c = 0, d1 = 0, d2 = 0, sum1 = 0, sum2 = 0, max_cal1 = 0, max_cal2 = 0;
    int i, n, j, index1 = 0, index2 = 0;
    scanf("%d""%ld", &n, &c);
    long int x[n], v[n];
    for(i = 0; i < n; i++){
        scanf("%ld""%ld", &x[i], &v[i]);
    }
    for(i = 0; i < n; i++){
        sum_c += v[i];
        if(max_cal1< (sum_c - x[i])){
            max_cal1 = sum_c - x[i];
            d1 = x[i];
            index1 = i;
        }
    }
    sum_c = 0;
    for(j = n - 1; j > index1; j--){
        sum_c += v[j];
        if(max_cal2 < sum_c - (c - x[j])){
            max_cal2 = sum_c - (c - x[j]);
            d2 = c - x[j];
            index2 = j
        }
    }
    printf("%d %d\n", i, j);
    sum1 = (max_cal1 - d1) + max_cal2;
    sum2 = max_cal1 + (max_cal2 - d2);
    printf("max_cal1:%ld\nmax_cal2:%ld\n", max_cal1, max_cal2);
    printf("d1:%ld\nd2:%ld\n", d1, d2);
    printf("%ld\n", max(sum1, sum2));
    return 0;
}