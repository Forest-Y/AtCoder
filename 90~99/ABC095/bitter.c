
#include<stdio.h>

int main(void){
    int n, cnt = 0, g, min= 1000;
    scanf("%d""%d", &n, &g);
    int nums[n];
    for(int i = 0; i < n; i++){
        scanf("%d", &nums[i]);
        g -= nums[i];
        if(min > nums[i]){
            min = nums[i];
        }
    }
    printf("%d\n", cnt = n + g / min);
    return 0;

}