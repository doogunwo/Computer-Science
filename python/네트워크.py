from collections import deque

def solution(n, computers):

    
    visited = [False]*n
    ans = 0

    for i in range(n):
        if not visited[i]:
            BFS(i,visited,n,computers)
            ans = ans +1
    return ans

def BFS(i,visited,n,computers):

    
    q = deque()
    q.append(i)

    while q:
        i = q.popleft()
        visited[i] = True
        for s in range(n):
            if computers[i][s]  and not visited[s]:
                q.append(s)


        

computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
n=3
ans = solution(n,computers)
print(ans)