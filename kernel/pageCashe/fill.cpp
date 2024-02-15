#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    // 읽을 파일 경로 설정
    string filename = "example.txt";

    // 파일 열기
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Unable to open file: " << filename << endl;
        return 1;
    }

    // 파일 읽기
    int line_count = 0;
    string line;
    while (getline(file, line)) {
        // 파일의 각 줄을 읽어서 무시
        line_count++;
    }

    // 파일 닫기
    file.close();

    cout << "lines : " << line_count<< endl;

    return 0;
}
