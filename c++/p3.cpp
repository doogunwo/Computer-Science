#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<int> num_list, int n) {
    int answer = 0;
    int i = 0;
    for(i=0; i<num_list.size(); i++){
        cout << num_list[i];
        if (num_list[i]  == n){
           cout << n ;
            answer = 1;
        }
        
    }
    
    return answer;
}


int main(){
    cout << "p3.cpp" ;
}