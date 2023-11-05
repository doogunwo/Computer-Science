
def DFS(k,cnt,dungeons,check):
    global answer
    answer = max(answer, cnt)
    for i in range(len(dungeons)):
        if check[i] == 0 and k>= dungeons[i][0]:
            check[i] = 1
            DFS(k-dungeons[i][1], cnt+1, dungeons, check)
            check[i] = 0

def solution(k, dungeons):
   global answer
   answer = 0
   dp = [0] * len(dungeons)
   DFS(k,0,dungeons,dp)

   return answer

k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]
result = solution(k, dungeons)
print(result)  # 결과는 3 (던전을 3번 탐험할 수 있음)
