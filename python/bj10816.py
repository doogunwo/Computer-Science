import sys

input = sys.stdin.readline

n = int(input())

n_list = list(map(int,input().split()))

m = int(input())

m_list = list(map(int,input().split()))

for i in m_list:
    count = 0
    target = i
    n_list = sorted(n_list)
    for j in n_list:
        if target == j:
            count = count +1
        
    print(count)

# import sys
# from bisect import bisect_left, bisect_right

# input = sys.stdin.readline

# n = int(input())
# n_list = list(map(int, input().split()))
# m = int(input())
# m_list = list(map(int, input().split()))

# # 정렬된 리스트 생성
# n_list.sort()

# for target in m_list:
#     # bisect_left와 bisect_right를 사용하여 이진 탐색
#     count = bisect_right(n_list, target) - bisect_left(n_list, target)
#     print(count)

# from collections import Counter

# # 입력 받기
# n = int(input())
# cards = list(map(int, input().split()))
# m = int(input())
# targets = list(map(int, input().split()))

# # 카드의 개수 세기
# card_count = Counter(cards)

# # 결과 출력
# result = [card_count[target] for target in targets]
# print(" ".join(map(str, result)))
