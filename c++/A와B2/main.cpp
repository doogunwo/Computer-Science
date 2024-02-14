#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

// 함수 선언: T에서 시작하여 S를 만들 수 있는지 재귀적으로 확인하는 함수
bool canMake(string s, string t) {
    // 기저 조건: S와 T가 같아지면 성공
    if (s == t) return true;
    // T의 길이가 S의 길이보다 작아지면 실패
    if (t.length() < s.length()) return false;

    bool result = false;
    // T의 마지막 문자가 'A'인 경우: 'A'를 제거하고 재귀 호출
    if (t.back() == 'A') {
        result |= canMake(s, t.substr(0, t.length() - 1));
    }
    // T의 첫 문자가 'B'인 경우: 'B'를 제거하고 문자열을 뒤집은 뒤 재귀 호출
    if (t.front() == 'B') {
        reverse(t.begin(), t.end()); // 문자열 뒤집기
        t.pop_back(); // 마지막 문자(B) 제거
        result |= canMake(s, t);
    }
    return result;
}

int main() {
    string S, T;
    cin >> S >> T; // 문자열 S와 T 입력 받기

    // canMake 함수를 호출하여 결과 출력
    cout << (canMake(S, T) ? 1 : 0) << endl;
    return 0;
}
