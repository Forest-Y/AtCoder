
#include<stdio.h>

int main(void){
    int data[9], n, b;
    for(int i = 0; i < 9; i++){
        scanf("%d", &data[i]);
    }
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        scanf("%d", &b);
        for(int j = 0; j < 9; j++){
            if(data[j] == b){
                data[j] = 0;
                break;
            }
        }
    }
    if(data[0] == 0){
        if( (data[1] == 0 && data[2] == 0) || (data[3] == 0 && data[6] == 0) || (data[4] == 0 && data[8] == 0)){
            printf("Yes\n");
            return 0;
        }
    }else if(data[4] == 0){
        if( (data[3] == 0 && data[5] == 0) || (data[1] == 0 && data[7] == 0)  || (data[2] == 0 && data[6] == 0 )){
            printf("Yes\n");
            return 0;
        }
    }else if(data[8] == 0){
        if( (data[7] == 0 && data[6] == 0) || (data[5] == 0 && data[2] == 0) ){
            printf("Yes\n");
            return 0;
        }
    }
    printf("No\n");
    return 0;
}
