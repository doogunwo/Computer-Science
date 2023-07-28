def solution(num, total):
    answer = []
    answer.append(total//num)
    return answer


num = 4
total = 14

res = solution(num, total)
print(res)