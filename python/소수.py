A,B,N = map(int,input().split())
result = A/B
result_split = str(result).split(".")
print(result_split[1][N-1])
