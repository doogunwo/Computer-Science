#아이디어
#시간복잡도
#자료구조
#2Xn 크기 직사사각형을 1x2, 2x1타일로 채우는 방법의 수를 구하는 프로그램을 
#작성하시오.

import sys
input = sys.stdin.readline
n = int(input())
rs = [0,1,2]

for i in range(3,n+1):
    rs.append((rs[i-1]+rs[i-2])%10007)

print(rs[n])