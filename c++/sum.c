#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
int main(){

    time_t start, end;
    time(&start);
    int sum = 0; 
    for(int i = 0; i< 1000000; i++){
        sum = sum + i ;
    }

    time(&end);
    printf("sum=%d\n", sum);
    printf("time=%f\n", (float)(end-start));
    return 0;
}

