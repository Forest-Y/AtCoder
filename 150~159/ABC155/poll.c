
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int cmp(const void *a, const void *b){
    return strcmp((const char *)a, (const char *)b);
}

int main(void){
    int n, max = 0;
    scanf("%d", &n);
    char str[n][11];
    int count[n];
    for(int i = 0; i < n; i++){
        scanf("%s", str[i]);
        count[i] = 0;
    }
    qsort(str, n, 11, cmp);
    for(int i = 0; i < n - 1; i++){
        if(strcmp(str[i], str[i + 1]) == 0){
            count[i] ++;
            count[i + 1] = count[i] + 1;
        }
    }
    for(int i = 0; i < n; i++){
        if(count[i] > max){
            max = count[i];
        }
    }
    
    for(int i = 0; i < n; i++){
        if(max == count[i]){
            printf("%s\n", str[i]);
        }
    }
    return 0;
}