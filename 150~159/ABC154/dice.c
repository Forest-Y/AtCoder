
#include<stdio.h>

double calc_max(double data[], int n, int k){
    double max = 0, sum = 0;
    for(int i = 0; i <= n - k; i++){
        sum = 0;
        for(int j = 0; j < k; j++){
            sum += (data[i + j] + 1) / 2;
        }
        if(max < sum){
            max = sum;
        }
    }
    return max;
}

int main(void){
    int n, k;
    scanf("%d""%d", &n, &k);
    double data[n];
    for(int i = 0; i < n; i++){
        scanf("%lf", &data[i]);
    }
    printf("%lf\n", calc_max(data, n, k));
    return 0;

}