def solution(num, total):
    avg = total // num
    return [i for i in range(avg - (num-1)//2, avg + (num+2)//2)]

