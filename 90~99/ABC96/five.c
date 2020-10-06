
#include<stdio.h>

int judge_prime(int n){
    int divcnt = 0;
    for(int i = 1; i <= n; i++){
        if(n % i == 0){
            divcnt ++;
        }
    }
    if(divcnt == 2){
        return 1;
    }
    return 0;
}


void print_array(int data[], int n){
    for(int i = 0; i < n; i++){
        printf("%d ", data[i]);
    }
    printf("\n");
}

int main(void){
    int n, i = 0, j = 1;
    scanf("%d", &n);
    int data[n];
    while(i < n){
        if(judge_prime(j * 5 + 1)){
            data[i] = j * 5 + 1;
            i++;
        }
        j++;
    }
    print_array(data, n);
    return 0;
}
