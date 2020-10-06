
#include<stdio.h>

void make_seq(int flag[], int num[], int n, int k){
    int f;
    for(int i = 0; i < n; i++){
        f = flag[i];
        if(f == 0){
            flag[i] = 1;
            num[k] = i + 1;
            if(k == 1){
                for(int j = n; j > 0; j--){
                    printf("%d", num[j]);
                }
                printf("\n");
            }else{
                make_seq(flag, num, n, k - 1);
            }
            flag[i] = 0;
        }
    }
}

int main(void){
    int i, k;
    scanf("%d", &k);
    int flag[k], num[k], seq1[k], seq2[k];
    for(i = 0; i < k; i++){
        num[i] = flag[i] = 0;
    }
    make_seq(flag, num, k, k);
    return 0;

}