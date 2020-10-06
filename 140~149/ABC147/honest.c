
#include<stdio.h>

int main(void){
    int n, a, max = 0, score;
    scanf("%d", &n);
    int tes[n][n];
    for(int i = 0; i < n; i++){
        scanf("%d", &a);
        for(int j = 0; j < a; j++){
            int x, y;
            scanf("%d""%d", &x, &y);
            tes[i][x - 1] = y;
        }
    }
    for(int bit = 0; bit < (i << n); bit ++){
        score = 0;
        for(int i = 0; i < n; i++){
            if(bnit & (1 << i)){
                score ++;

            }
        }

    }

}