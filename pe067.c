#include<stdio.h>

#define row 100 
#define col 100 

int main(){
    int arr[101][101];

    for(int i = 0; i < row; i++){
        for(int j = 0; j<=i; j++){
            scanf("%d", &arr[i][j]);
        }
    }
   
    for(int i = row-2; i>=0; i--){
        for(int j = 0; j<=i; j++){
            if(arr[i][j]+arr[i+1][j] > arr[i][j] + arr[i+1][j+1])
                arr[i][j] += arr[i+1][j];
            else
                arr[i][j] += arr[i+1][j+1];
        }
    }

    printf("%d\n", arr[0][0]);

    return 0;
}
