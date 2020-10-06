
#include<stdio.h>

void set_num(int data[], int n){
    for(int i = 0; i < n; i++){
        scanf("%d", &data[i]);
    }
}

void count_block(int block[], int n){
    int cnt = 0, num = 1;
    for(int i = 0; i < n; i++){
        if(block[i] != num){
            cnt ++;
        }else{
            num ++;
        }
    }
    if(num == 1){
        printf("%d\n", -1);
        return ;
    }
    printf("%d\n", cnt);
}

int main(void){
    int n;
    scanf("%d", &n);
    int block[n];
    set_num(block, n);
    count_block(block, n);
    return 0;

}