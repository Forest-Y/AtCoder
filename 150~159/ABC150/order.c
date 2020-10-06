
#include<stdio.h>
#include<stdlib.h>

int cnt1 = 0, cnt2 = 0;
void make_seq(int flag[], int num[], int seq1[], int seq2[], int n, int k){
    int f, judge = 1;
    for(int i = 0; i < n; i++){
        f = flag[i];
        if(f == 0){
            flag[i] = 1;
            num[n - k] = i + 1;
            if(k == 1){
                cnt2 ++;
                for(int j = n - 1; j >= 0; j--){
                    if(seq1[j] != num[j]){
                        judge = 0;
                        break;
                    }
                }
                if(judge == 0){
                    judge = 1;
                    for(int j = n - 1; j >= 0; j--){
                        if(seq2[j] != num[j]){
                            judge = 0;
                            break;
                        }
                    }
                }
                if(judge == 1){
                    if(cnt1 == 0){
                        cnt1 = cnt2;
                    }else{
                        printf("%d\n", abs(cnt1 - cnt2));
                        exit(0);
                    }
                }
            }else{
                make_seq(flag, num, seq1, seq2, n, k - 1);
            }
            flag[i] = 0;
        }
    }
}

void set_seq(int seq[], int n){
    for(int i = 0; i < n; i++){
        scanf("%d", &seq[i]);
    }
}

int main(void){
    int i, n, judge = 1;
    scanf("%d", &n);
    int flag[n], num[n], seq1[n], seq2[n];
    set_seq(seq1, n);
    set_seq(seq2, n);

    for(int i = 0; i < n; i++){
        num[i] = flag[i] = 0;
    }

    for(int i = 0; i < n; i++){
        if(seq1[i] != seq2[i]){
            judge = 0;
            break;
        }
    }
    if(judge){
        printf("%d\n", 0);
    }
    make_seq(flag, num, seq1, seq2, n, n);
    return 0;

}