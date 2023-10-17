def solution(a, b, n):
    answer  = 0
    # 기본 로직
    
    while(n>=a):
        remain_bottle = n%a
        n = (n//a) * b
        answer = answer +n
        n = n + remain_bottle
    return answer


a=2 # 빈병 2개를 주면 
b=1 # 콜라 1개르 준다.
n=20 # 빈병

solution(a,b,n)
