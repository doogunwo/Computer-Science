#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int T, N;
    cin >> T; // 테스트 케이스의 수를 입력받습니다.

    for(int t = 1; t <= T; ++t) {
        cin >> N; // 각 테스트 케이스의 카드 수를 입력받습니다.
        vector<string> cards(N);

        for(int i = 0; i < N; ++i) {
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // 이전 입력 후 남아있는 개행 문자 무시
            getline(cin, cards[i]); // 카드 이름을 입력받습니다.
        }

        int cost = 0;
        for(int i = 1; i < N; ++i) {
            if(cards[i] < cards[i-1]) { // 현재 카드가 이전 카드보다 사전순으로 앞서는 경우
                cost++; // 비용 증가
                sort(cards.begin(), cards.begin() + i + 1); // 해당 카드까지의 부분을 정렬합니다.
            }
        }

        cout << "Case #" << t << ": " << cost << endl; // 결과 출력
    }

    return 0;
}
