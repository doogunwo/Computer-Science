def solution(x,n):
    
    answer = []
    print(answer)
    for i in range(n):
        answer.append(x+(x*i))
    
    print(answer)
    return answer


x=2
n=5
solution(x,n)