
#include<stdio.h>
#include<string.h>

int main(void){
    char now[5];
    char day[7][5] = {"SAT", "FRI", "THU", "WED", "TUE", "MON", "SUN"};
    scanf("%s", now);
    for(int i = 0; i < 7; i++){
        if(strcmp(day[i], now) == 0){
            printf("%d\n", i + 1);
            return 0;
        }
    }
    return 0;
}