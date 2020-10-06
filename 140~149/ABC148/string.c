
#include<stdio.h>

int main(void){
    int n;
    scanf("%d", &n);
    char s[n + 1], t[n + 1];
    scanf("%s""%s", s, t);
    for(int i = 0; i < n; i++){
        printf("%c%c", s[i], t[i]);
    }
    printf("\n");
    return 0;
}