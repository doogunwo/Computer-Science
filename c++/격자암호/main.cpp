#include <iostream>
#include <vector>
#include <string>

// 격자 암호화 함수
std::string encrypt(const std::string& plaintext, const std::vector<std::vector<char>>& grid) {
    std::string ciphertext;
    for (char c : plaintext) {
        // 각 문자에 대해 격자 상의 위치를 확인하고 암호문으로 변환
        for (const auto& row : grid) {
            for (char ch : row) {
                if (ch == c) {
                    ciphertext += std::to_string(&row - &grid[0]) + std::to_string(&ch - &row[0]);
                    break;
                }
            }
        }
    }
    return ciphertext;
}

// 격자 암호 해독 함수
std::string decrypt(const std::string& ciphertext, const std::vector<std::vector<char>>& grid) {
    std::string plaintext;
    for (size_t i = 0; i < ciphertext.length(); i += 2) {
        int row = ciphertext[i] - '0';
        int col = ciphertext[i + 1] - '0';
        plaintext += grid[row][col];
    }
    return plaintext;
}

int main() {
    // 격자 생성
    std::vector<std::vector<char>> grid = {
        {'a', 'b', 'c'},
        {'d', 'e', 'f'},
        {'g', 'h', 'i'}
    };

    // 평문 및 암호문 정의
    std::string plaintext = "hello";
    std::string ciphertext = encrypt(plaintext, grid);

    // 암호문 출력
    std::cout << "Encrypted: " << ciphertext << std::endl;

    // 암호문 해독
    std::string decrypted = decrypt(ciphertext, grid);

    // 평문 출력
    std::cout << "Decrypted: " << decrypted << std::endl;

    return 0;
}
