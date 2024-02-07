def count_zeros_in_factorial(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count
#10! =  3,628,800 이다. 이 때 처음  왼쪽에서부터 처음 등장하는 0은 2번째자리가 된다. 2번째= 정답
n = int(input())
zeros = count_zeros_in_factorial(n)
print(zeros)
