
#include<stdio.h>

long int calc_gcd(long int a, long int b){
    long int temp, r, x;
    if(a < b){
        temp = a;
        a = b;
        b = temp;
    }
    x = a * b;
    r = a % b;
    while(r != 0){
        a = b;
        b = r;
        r = a % b;
    }
    return x / b;
}

long int  set_data(int n){
    long int l, a;
    for(int i = 0; i < n; i++){
        scanf("%ld", &a);
        if(i == 0){
            l = a;
        }else{
            l = calc_gcd(l, a);
        }
    }
    return l;
}

/*void count_SCM(long int data[], int n, long int m){
    int cnt = 0, judge = 1;
    long int gcd = 1;
    gcd = calc_gcd(data, n);
    printf("%d\n", (int)((double)m / gcd + 0.5));
}*/

void print_array(long int data[], int n){
    for(int i = 0; i < n; i++){
        printf("%ld ", data[i]);
    }
    printf("\n");
}

int main(void){
    int n;
    long int m, gcd;
    scanf("%d""%ld", &n, &m);
    long int data[n];
    gcd = set_data(n);
    /*print_array(data, n);*/
    if(gcd > m){
        printf("%d\n", 0);
        return 0;
    }
    printf("%ld\n", (long int)((double)m / gcd + 1));
    return 0;

}