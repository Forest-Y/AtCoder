
#include<stdio.h>

int main(void){
    int n;
    scanf("%d", &n);
    int data[n];
    for(int i = 0; i < n; i++){
        scanf("%d", &data[i]);
    }
    for(int i = 0; i < n; i++){
        if(data[i] % 2 == 0 && (data[i] % 3 != 0 && data[i] % 5 != 0)){
            printf("DENIED\n");
            return 0;
        }
    }
    printf("APPROVED\n");
    return 0;
}