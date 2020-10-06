
#include<stdio.h>
#include<string.h>

int main(void){
    int n, len;
    char s[10005];
    scanf("%d", &n);
    scanf("%s", s);
    len = strlen(s);
    for(int i = 0; i < len; i++){
        s[i] += n;
        if(s[i] > 'Z'){
            s[i] = s[i] -('Z' - 'A' + 1);
        }
    }
    printf("%s\n", s);
    return 0;
}