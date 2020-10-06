#include<stdio.h>
 
/* void judge(int data[], int n){
    for(int i = 1; i < n; i++){
        for(int j = 0; j < i; j++){
            if(data[i] == data[j]){
                printf("NO\n");
                return ;
            }
        }
    }
    printf("YES\n");
    return ;
}
*/


#define SWAP(type,a,b) { type work = a; a = b; b = work; }

/*
    基準値を選ぶ
*/
int select_pivot(const int* array, int begin, int end)
{
    return array[(begin + end) / 2];  // 中央の要素を基準値とする
}


/*
    クイックソート (再帰部分、昇順)
*/
void quick_sort_rec(int* array, int begin, int end)
{
    int pivot = select_pivot( array, begin, end );
    int i = begin;
    int j = end;

    while( 1 ){
        while( array[i] < pivot ){ ++i; }  // 基準値以上の値が見つかるまで右方向へ進めていく
        while( array[j] > pivot ){ --j; }  // 基準値以下の値が見つかるまで左方向へ進めていく

        if( i >= j ){ break; }  // 左右から進めてきたiとjがぶつかったらループを終える

        // 基準値の位置よりも左側にあり、基準値よりも大きい値 (array[i]) と、
        // 基準値の位置よりも右側にあり、基準値よりも小さい値 (array[j]) の
        // 位置関係を交換する。
        SWAP( int, array[i], array[j] );

        // 次回に備えて、注目点をずらす
        i++;
        j--;
    }


    // 基準値の位置より左側に要素が２つ以上あれば、
    // その部分についてクイックソートを再帰させる
    if( i - begin >= 2 ){
        quick_sort_rec( array, begin, i - 1 );
    }

    // 基準値の位置より右側に要素が２つ以上あれば、
    // その部分についてクイックソートを再帰させる
    if( end - j >= 2 ){
        quick_sort_rec( array, j + 1, end );
    }
}


void sort(int* array, int size){
    // 配列全体を対象にする
    quick_sort_rec( array, 0, (int)(size - 1) );
}

int main(void){
    int n, judge = 1;
    scanf("%d", &n);
    int data[n];
    for(int i = 0; i < n; i++){
        scanf("%d", &data[i]);
    }
    sort(data, n);
    for(int i = 0; i < n - 1; i++){
        if(data[i] == data[i + 1]){
            printf("NO\n");
            return 0;
        }
    }
    printf("YES\n");
    return 0;
}