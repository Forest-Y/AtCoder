
#include<stdio.h>

void set_data(int data[], int n){
    for(int i = 0; i < n; i++){
        scanf("%d", &data[i]);
    }
}

int calc_dis(int data[], int n, int mean){
    int dis = 0;
    for(int i = 0; i < n; i++){
        dis += (mean - data[i]) * (mean - data[i]);
    }
    return dis;
}
int main(void){
    int n, sum = 0;
    scanf("%d", &n);
    int data[n];
    set_data(data, n);
    for(int i = 0; i < n; i++){
        sum += data[i];
    }
    printf("%d\n", calc_dis(data, n, (double)sum / n + 0.5));
    return 0;
}