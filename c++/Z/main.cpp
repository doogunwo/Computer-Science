#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int N, r, c;
    cin >> N >> r >> c;

    int cnt = 0;
    int size = 1 << N; // 배열의 크기 계산

    for (int i = 0; i < N; ++i) {
        int newSize = size / 2; // 현재 배열의 절반 크기

        // 현재 위치가 몇 사분면에 속하는지 계산
        int area = 0;
        if (r >= newSize) {
            area += 2;
            r -= newSize;
        }
        if (c >= newSize) {
            area += 1;
            c -= newSize;
        }

        // 현재 사분면으로 이동
        cnt += newSize * newSize * area;

        size = newSize; // 다음 사분면으로 이동
    }

    cout << cnt << endl;

    return 0;
}
