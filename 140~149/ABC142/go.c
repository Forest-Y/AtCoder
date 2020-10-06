
#include<stdio.h>

int main(void){
    int n;
    scanf("%d", &n);
    int x, order[n];
    for(int i = 0; i < n; i++){
        scanf("%d", &x);
        order[x - 1] = i + 1;
    }
    for(int i = 0; i < n; i++){
        printf("%d ", order[i]);
    }
    printf("\n");
    return 0;
    
}