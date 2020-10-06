
#include<stdio.h>

int search_max(int nums[]){
    int x = 0, max = nums[0];
    for(int i = 0; i < 3; i++){
        if(max < nums[i]){
            x = i;
            max = nums[i];
        }
    }
    return x;
}
int main(void){
    int k, nums[5], index, sum = 0;

    for(int i = 0; i < 3; i++){
        scanf("%d", &nums[i]);
    }

    scanf("%d", &k);
    index = search_max(nums);
    for(int i = 0; i < k; i++){
        nums[index] *= 2;
    }
    for(int i = 0; i < 3; i++){
        sum += nums[i];
    }
    printf("%d\n", sum);
    return 0;
}