
#include<stdio.h>

int main(void){
    for(int i = 0; i < 5; i++){
        for(int j = 0; j < 5; j++){
            if(j == 2){
                break;
            }
            printf("%d %d\n", i, j);
        }
    }
    return 0;
}