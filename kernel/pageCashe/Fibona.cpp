#include <iostream>

// 컴파일 타임 피보나치 수열 계산
template <int N>
struct Fibonacci {
    static const int value = Fibonacci<N - 1>::value + Fibonacci<N - 2>::value;
};

// 특수화를 통한 기저 조건 설정
template <>
struct Fibonacci<0> {
    static const int value = 0;
};

template <>
struct Fibonacci<1> {
    static const int value = 1;
};

// 메인 함수
int main() {
    std::cout << "Fibonacci of Number: " << Fibonacci<40>::value << std::endl;
    return 0;
}
