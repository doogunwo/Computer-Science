#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int n) {
    int answer = 0;
    int i = 0;
    int num[5] =  {1,2,3,4,5};
    for(i=0; i<5; i++){

        if (num[i]  == n){
            answer = 1;
        }
        
    }

    return answer;
}


int main (){
    int res= solution(3);
    cout<< res << endl;
    system("pause");
}