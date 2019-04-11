//code created by NamanNimmo Gera.
//10:32pm, April 10, 2019.

#include<bits/stdc++.h>
using namespace std;
#define MAX 10000000000
#define LL long long int

int main(){
     LL i,j,flag;
     for(i=20;i<MAX;i++){
        flag=1;          //you can also take out the LCM OF THE all the numbers recursively :), will get the same answer
        for(j=1;j<=20;j++){ //I will stick with the brute force :P
            if(i%j != 0){
                flag=0;
                break;
            }
        }
        if(flag==1){ 
            printf("%lld\n",i);//this will print 232792560
            break;
        }
      }
    return 0;
}
