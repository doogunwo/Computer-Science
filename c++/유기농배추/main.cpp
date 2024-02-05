#include <iostream>
#include <vector>
using namespace std;

vector<vector<int> > map;
vector<vector<bool> > visited;
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
int N, M;

void dfs(int x, int y) {
    visited[x][y] = true;
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (nx >= 0 && nx < N && ny >= 0 && ny < M && map[nx][ny] == 1 && !visited[nx][ny]) {
            dfs(nx, ny);
        }
    }
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        int K, count = 0;
        cin >> M >> N >> K;
        map.assign(N, vector<int>(M, 0));
        visited.assign(N, vector<bool>(M, false));
        
        for (int i = 0; i < K; i++) {
            int x, y;
            cin >> y >> x; // 주의: 입력 순서
            map[x][y] = 1;
        }
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] == 1 && !visited[i][j]) {
                    dfs(i, j);
                    count++;
                }
            }
        }
        
        cout << count << "\n";
    }
    return 0;
}
