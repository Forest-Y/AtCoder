
#include<stdio.h>


#define SWAP(type,a,b) { type work = a; a = b; b = work; }

/*
    基準値を選ぶ
*/
long int select_pivot(long int* array, long int begin, long int end)
{
    return array[(begin + end) / 2];  // 中央の要素を基準値とする
}


/*
    クイックソート (再帰部分、昇順)
*/
void quick_sort_rec(long int* array, long int begin, long int end)
{
    long int pivot = select_pivot( array, begin, end );
    long int i = begin;
    long int j = end;

    while( 1 ){
        while( array[i] < pivot ){ ++i; }  // 基準値以上の値が見つかるまで右方向へ進めていく
        while( array[j] > pivot ){ --j; }  // 基準値以下の値が見つかるまで左方向へ進めていく

        if( i >= j ){ break; }  // 左右から進めてきたiとjがぶつかったらループを終える

        // 基準値の位置よりも左側にあり、基準値よりも大きい値 (array[i]) と、
        // 基準値の位置よりも右側にあり、基準値よりも小さい値 (array[j]) の
        // 位置関係を交換する。
        SWAP(long int, array[i], array[j] );

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


void sort(long int* array, long int size){
    // 配列全体を対象にする
    quick_sort_rec( array, 0, (long int)(size - 1) );
}

void set_data(long int data[], long int n){
    for(long int i = 0; i < n; i++){
        scanf("%ld", &data[i]);
    }
}

void calc_data(long int data[], long int pair[], long int n){
    long int x = 0;
    for(long int i = 0; i < n; i++){
        for(long int j = 0; j < i; j++){
            pair[x] = data[i] * data[j];
            /*printf("%ld ", pair[x]);*/
            x++;
        }
    }
    /*printf("\n");*/
}

void print_array(long int data[], long int n){
    for(long int i = 0; i < n; i++){
        printf("%ld ", data[i]);
    }
    printf("\n");
}

int main(void){
    long int n, k;
    scanf("%ld""%ld", &n, &k);
    long int data[n], pairs[(n * (n - 1)) / 2];
    set_data(data, n);
    /*print_array(data, n);*/
    calc_data(data, pairs, n);

    /*print_array(pairs, (n * (n - 1)) / 2);*/
    sort(pairs, (n * (n - 1)) / 2 );
    
    printf("%ld\n", pairs[k - 1]);
}