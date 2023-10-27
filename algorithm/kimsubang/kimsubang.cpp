#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

string solution(vector<string> seoul) {
    
    auto it = find(seoul.begin(), seoul.end(), "Kim");
    if(it != seoul.end()){
        int index = distance(seoul.begin(),it);
        return "김서방은 " + to_string(index) + "에 있다";
    }
}

int main(){
    vector<string> v;
    v.push_back("Jane");
    v.push_back("Kim");
    solution(v);
}