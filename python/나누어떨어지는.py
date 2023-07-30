def solution(arr, div):
    answer = []

    for j in arr:
        if j%div==0:
            answer.append(j)
        else:
            pass
    if len(answer) <1 :
        answer.append(-1)
    else:
        answer.sort()
    return answer

arr = [2, 36, 1, 3]
div  = 1
solution(arr,div)