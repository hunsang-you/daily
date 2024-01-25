'''
7
1 6
6 3
3 5
4 1
2 4
4 7
'''
import sys
from collections import deque

def bfs():
    while queue:
        now = queue.popleft()
        for i in graph[now] :
            if ans[i] == 0:
                ans[i] = now
                queue.append(i)

N = int(input())
graph = [[] for _ in range(N+1)]
V = N - 1
for _ in range(V):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

queue = deque()
queue.append(1)

ans = [0] * (N+1)

bfs()

for i in range(2, len(ans)):
    print(ans[i])