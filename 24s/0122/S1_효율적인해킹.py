'''
5 4
3 1
3 2
4 3
5 3
'''
# BFS, DFS

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[v].append(u)


def BFS(s):
    queue = deque()
    queue.append(s)
    cnt = 0
    visited = [0] * (N+1)
    visited[s] = 1

    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
                cnt += 1
    return cnt

result = []
maxCnt = 1

for i in range(1, N+1):
    cnt = BFS(i)
    if cnt > maxCnt:
        maxCnt = cnt
        result = []
        result.append(i)

    elif cnt == maxCnt:
        result.append(i)

print(*result)