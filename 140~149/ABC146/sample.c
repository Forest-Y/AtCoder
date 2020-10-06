#include<stdio.h>

int main(void){
    long int a = 25000000000;
    if(a * 2 + 1 * 11 < 100000000000){
        printf("true\n");
    }else{
        printf("false\n");
    }
    return 0;
}