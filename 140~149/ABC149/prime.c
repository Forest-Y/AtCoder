
#include<stdio.h>

void next_prime(int x){
    int divcnt = 0;
    while(1){
        divcnt = 0;
        for(int i = 1; i <= x; i++){
            if(x % i == 0){
                divcnt ++;
                if(divcnt > 2){
                    break;
                }
            }
        }
        if(divcnt == 2){
            printf("%d\n", x);
            return;
        }
        x++;
    }
}

int main(void){
    int x;
    scanf("%d", &x);
    next_prime(x);
    return 0;
}