def solution(k, score):
           
    answer = []
    HallOfFame = []
    
    for i in score:
        if len(HallOfFame) <k:
            HallOfFame.append(i)
        else:
            if min(HallOfFame) < i:
                HallOfFame.remove(min(HallOfFame))
                HallOfFame.append(i)
        answer.append(min(HallOfFame))

    return answer

res= solution(3,[10, 100, 20, 150, 1, 100, 200])
print(res)