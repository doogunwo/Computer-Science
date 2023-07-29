#include <string>
#include <vector>
#include <iostream>
/*
문자열 곱하기

*/
using namespace std;

string solution(string my_string, int k) {
    string answer = "";

    for(int i=0; i<k; i++){
        answer = answer + my_string;    
    }
    return answer;
}

main(){
        string my_string = "string";
        int k= 3;

        solution(my_string,k);
        system("pause");
}

