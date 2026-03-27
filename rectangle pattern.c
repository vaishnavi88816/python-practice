#include stdio.h
int main(){
    int x;
    int y;
    print("enter number of rows:");
    scanf("%d",&n);
    printf("print the number of column:");
    scanf("%d",&m);
    for(int i=1;i<=n;i++){
    for(int j=1; j<=m; j++){
        printf("*");
    }
    printf("*");
}
return 0;
}