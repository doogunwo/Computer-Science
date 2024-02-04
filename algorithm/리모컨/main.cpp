#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

bool broken[10]; // 고장난 버튼은 true

// target 채널로 이동할 수 있는지 확인하고, 이동할 수 있다면 숫자 버튼 클릭 수를 반환
int canMove(int target) {
    if (target == 0) {
        return broken[0] ? 0 : 1;
    }
    int len = 0;
    while (target > 0) {
        if (broken[target % 10]) return 0; // 고장난 버튼이면 이동 불가
        len += 1; // 버튼 클릭 수 증가
        target /= 10;
    }
    return len;
}

int main() {
    int N, M;
    cin >> N >> M;
    for (int i = 0; i < M; i++) {
        int a;
        cin >> a;
        broken[a] = true; // 고장난 버튼 표시
    }

    // +/- 버튼만 사용하는 경우
    int result = abs(N - 100);
    
    // 모든 채널을 순회하며 확인
    for (int i = 0; i <= 1000000; i++) { // N의 최대값 + 여유분
        int len = canMove(i); // i 채널로 이동 가능한지 확인
        if (len > 0) {
            int press = abs(i - N); // i에서 N까지 +/- 버튼으로 이동하는 클릭 수
            result = min(result, len + press);
        }
    }

    cout << result;
    return 0;
}
