#include <iostream>
#include <string>

/*
대소문자 바꿔서 출력하기

대->소
소->대
*/


using namespace std;

int main(){
    string str;
    cin >> str;

    for(int i = 0; i<str.size(); i++){
        if ( 'A'<= str[i] && str[i] <='Z'){
            str[i] = str[i] +32;
        }
        else{
            str[i] =  str[i] -32;
        }
    }
    cout << str;
    system("pause");

    return 0;
}