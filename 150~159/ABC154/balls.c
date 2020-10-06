
#include<stdio.h>
#include<string.h>

int main(void){
    int cnt1, cnt2;
    char s[15], t[15], u[15];
    scanf("%s""%s", s, t);
    scanf("%d""%d", &cnt1, &cnt2);
    scanf("%s", u);
    if(strcmp(s, u) == 0){
        cnt1 -= 1;
    }else{
        cnt2 -= 1;
    }
    printf("%d %d\n", cnt1, cnt2);
    return 0;
}