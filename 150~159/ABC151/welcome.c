
#include<stdio.h>
#include<string.h>


#define SWAP(type,a,b) { type work = a; a = b; b = work; }

/*
    基準値を選ぶ
*/
int select_pivot(int* array, int begin, int end)
{
    return array[(begin + end) / 2];  // 中央の要素を基準値とする
}


/*
    クイックソート (再帰部分、昇順)
*/
void quick_sort_rec(int* array,char results[][5], int begin, int end)
{
    long int pivot = select_pivot( array, begin, end );
    int i = begin;
    int j = end;
    char temp[5];

    while( 1 ){
        while( array[i] < pivot ){ ++i; }  // 基準値以上の値が見つかるまで右方向へ進めていく
        while( array[j] > pivot ){ --j; }  // 基準値以下の値が見つかるまで左方向へ進めていく

        if( i >= j ){ break; }  // 左右から進めてきたiとjがぶつかったらループを終える

        // 基準値の位置よりも左側にあり、基準値よりも大きい値 (array[i]) と、
        // 基準値の位置よりも右側にあり、基準値よりも小さい値 (array[j]) の
        // 位置関係を交換する。
        SWAP( int, array[i], array[j] );
        strcpy(temp, results[i]);
        strcpy(results[i], results[j]);
        strcpy(results[j], temp);

        // 次回に備えて、注目点をずらす
        i++;
        j--;
    }


    // 基準値の位置より左側に要素が２つ以上あれば、
    // その部分についてクイックソートを再帰させる
    if( i - begin >= 2 ){
        quick_sort_rec( array, results, begin, i - 1 );
    }

    // 基準値の位置より右側に要素が２つ以上あれば、
    // その部分についてクイックソートを再帰させる
    if( end - j >= 2 ){
        quick_sort_rec( array, results, j + 1, end );
    }
}

void sort(int array[], char results[][5], int size){
    // 配列全体を対象にする
    quick_sort_rec( array, results, 0, (int)(size - 1) );
}

void print_array(int data[],char result[][5], int n){
    for(int i = 0; i < n; i++){
        printf("%d %s\n", data[i], result[i]);
    }
    printf("\n");
}

void counts(int data[], char results[][5], int n, int m){
    int cnt_a = 0, cnt_w = 0, cnt = 0, x, p[n], flag[n];
    char ac[5] = "AC";
    for(int i = 0; i < n; i++){
        p[i] = 0;
        flag[i] = 0;
    }
    for(int i = 0; i < m; i++){
        if(strcmp(results[i], ac) == 0 && flag[data[i] - 1] == 0){
            cnt_a ++;
            x = data[i];
            cnt_w += p[data[i] - 1];
            flag[data[i] - 1] = 1;
        }else{
            p[data[i] - 1] ++;
        }
    }
    printf("%d %d\n", cnt_a, cnt_w);
}

int main(void){
    int n, m;
    scanf("%d""%d", &n, &m);
    if(m == 0){
        printf("%d %d\n", 0, 0);
        return 0;
    }
    int num[m];
    char results[m][5];
    for(int i = 0; i < m; i++){
        scanf("%d""%s", &num[i], results[i]);

    }
    /*sort(num, results, m);
    print_array(num, results, m); */
    counts(num, results, n, m);
    return 0;
}