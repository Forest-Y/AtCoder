
#include<stdio.h>
#include<math.h>

int main(void){
    int n, p = 1;
    scanf("%d", &n);
    for(int i = 1; i <= n; i++){
        p *= i;
    }
    /*printf("%d\n", p);*/
    int dis[n][2];
    double sum = 0;
    for(int i = 0; i < n; i++){
        scanf("%d""%d", &dis[i][0], &dis[i][1]);
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(i != j){
                /*printf("%d->%d:%lf\n", i + 1, j + 1, sqrt((dis[i][0] - dis[j][0] ) * (dis[i][0] - dis[j][0] ) + (dis[i][1] - dis[j][1] ) * (dis[i][1] - dis[j][1] )));*/
                sum += sqrt( (dis[i][0] - dis[j][0] ) * (dis[i][0] - dis[j][0] ) + (dis[i][1] - dis[j][1] ) * (dis[i][1] - dis[j][1] ) ) * p / n;
            }
        }
    }
    /*printf("%lf\n", sum);*/
    printf("%lf\n", (double)sum / p);
    return 0;
}