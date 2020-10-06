
#include<stdio.h>
#include<string.h>

int main(void){
    char str[101];
    int cnt = 0,len;
    scanf("%s", str);
    len = strlen(str);
    for(int i = 0; i < len / 2; i++){
        if(str[i] != str[len - i - 1]){
            cnt ++;
        }
    }
    printf("%d\n", cnt);
    return 0;
}