def solution(t, p):
    answer = 0
    for i in range(0,len(t)+1-len(p)):
        
        if t[i:i+len(p)] <= p:
                answer = answer+1
      
    print(answer)
    return answer

t ="500220839878"
p = "7"

solution(t,p)