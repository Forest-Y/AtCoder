
#include<stdio.h>

int main(void){
    int n, q, a;
    long int k;
    scanf("%d""%ld""%d", &n, &k, &q);
    long int data[n];
    for(int i = 0; i < n; i++){
        data[i] = 0;
    }
    /*for(int i = 0; i < n; i++){
        printf("%ld \n", data[i]);
    }
    printf("\n");*/
    for(int i = 0; i < q; i++){
        scanf("%d", &a);
        data[a - 1] += 1;
    }
    for(int i = 0; i < n; i++){
        if(q - data[i] >= k){
            printf("No\n");
        }else{
            printf("Yes\n");
        }
    }
    return 0;
}