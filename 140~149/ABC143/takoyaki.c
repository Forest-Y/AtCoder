#include<stdio.h>

void set_data(int data[], int n){
    for(int i = 0; i < n; i++){
        scanf("%d", &data[i]);
    }
}

int calc(int data[], int n){
    int sum = 0;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < i; j++){
            sum += data[i] *data[j];
        }
    }
    return sum;
}

int main(void){
    int n;
    scanf("%d", &n);
    int takoyaki[n];
    set_data(takoyaki, n);
    printf("%d\n", calc(takoyaki, n));
    return 0;

}