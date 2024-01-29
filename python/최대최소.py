def solution(a, b):

    def gcd(a,b):
        while b> 0:
            a,b = b,a%b
        return a
    
    def lcm(a,b):
        return a*b  / gcd(a,b)
        
    return [gcd(a,b),lcm(a,b)]

n = 3
m = 12
solution(n,m)