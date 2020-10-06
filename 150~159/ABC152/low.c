
#include<stdio.h>

int main(void){
    long int n;
    int cnt = 0, min = 20000000;
    scanf("%ld", &n);
    long int data[n];
    for(int i = 0; i < n; i++){
        scanf("%ld", &data[i]);
        if(min >= data[i]){
            cnt ++;
            min = data[i];
        }
    }
    printf("%d\n", cnt);
    return 0;

}