from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

graph = []
node = []
for i in range(n-1):
    point1, point2, length = map(int,input().split())
    graph.append((point1,point2,length))

for _ in range(m):
    node1,node2 =map(int,input().split())
    node.append((node1,node2))

