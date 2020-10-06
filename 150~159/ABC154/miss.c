
#include<stdio.h>

void judge(int data[]){
    for(int i = 1; i < n; i++){
        for(int j = 0; j < i; j++){
            if(data[i] == data[j]){
                printf("No\n");
                return ;
            }
        }
    }
    printf("Yes\n");
    return ;
}

int main(void){
    int n;
    scanf("%d", &n);
    int data[n];
    for(int i = 0; i < n; i++){
        scanf("%d", &data[i]);
    }
    judge(data, n);
    return 0;
}