#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int T, N;
    cin >> T;
    vector<string> output(T);

    for (int t = 1; t <= T; t++) {
        cin >> N;
        cin.ignore(); 
        vector<string> cards(N);

        for (int j = 0; j < N; j++) {
            getline(cin, cards[j]); 
        }

        int cost = 0;
        for (int i = 1; i < N; i++) {
            if (cards[i] < cards[i - 1]) {
                cost += 1;
                sort(cards.begin(), cards.begin() + i + 1);
            }
        }

        output[t - 1] = "Case #" + to_string(t) + ": " + to_string(cost);
    }

    for (int k = 0; k < T; k++) {
        cout << output[k] << endl; 
    }
}
