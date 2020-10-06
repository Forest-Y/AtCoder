
#include<stdio.h>

int main(void){
    int n, judge = 1;;
    scanf("%d", &n);
    long int data[n], memo[1000000000];
    for(int i = 0; i < n; i++){
        scanf("%ld", &data[i]);
        if(judge == 1){
            if(memo[data[i]] ==data[i]){
                judge = 0;;

            }else{
                memo[data[i]] = data[i];
            }
        }
    }
    if(judge == 1){
        printf("YES\n");
    }else{
        printf("NO\n");
    }
    return 0;
}