
#include<stdio.h>

void count(char s[], int n){
    int cnt = 0;
    for(int i = 0; i < n - 2; i++){
        if(s[i] == 'A' && s[i + 1] == 'B' && s[i + 2] == 'C'){
            cnt ++;
            i += 2;
        }
    }
    printf("%d\n", cnt);
}

int main(void){
    int n;
    scanf("%d", &n);
    char s[n + 1];
    scanf("%s", s);
    count(s, n);
    return 0;
}