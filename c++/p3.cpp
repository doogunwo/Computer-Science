#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr, int k) {
    vector<int> answer;
    
    for(int i=0; i<arr.size(); i++){
        if(k%2==0){
            int val = arr[i] + k;
            answer.push_back(val);
        }
        else{
            int val = arr[i] * k;
            answer.push_back(val);
        }
        
    }

    return answer;
}


int main(){

    system("pause");
}