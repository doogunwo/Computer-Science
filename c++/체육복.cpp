#include <string>
#include <vector>
#include <iostream>
using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
        
}

int main(){
    int n =5;
    vector<int> lost;
    lost.push_back(2);
    lost.push_back(4);
    vector<int> reserve;
    reserve.push_back(1);
    reserve.push_back(3);
    reserve.push_back(5);
    int res = solution(n,lost,reserve);
    cout << res;
}