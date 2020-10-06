
#include<stdio.h>

int main(void){
    int n, cnt = 0, i;
    scanf("%d", &n);
    char s[n + 1];
    scanf("%s", s);
    for(i = 0; i < n - 1; i++){
        if(i == 0){
            cnt++;
        }else if(s[i] != s[i - 1]){
            cnt++;
        }
        
    }
    if(i == n - 1 && s[i] != s[i - 1]){
        cnt++;
    }
    printf("%d\n", cnt);
    return 0;
}