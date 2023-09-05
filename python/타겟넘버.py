def solution(numbers, target):
    global answer # 전역변수 사용한다는 선언
    dfs(0, numbers, target, 0)
    return answer


