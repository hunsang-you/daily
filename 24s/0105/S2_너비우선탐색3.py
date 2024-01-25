'''
5 5 1
1 4
1 2
2 3
2 4
3 4

'''
# BFS
import sys
input = sys.stdin.readline
from collections import deque

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [-1] * (N+1)

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort()

def BFS(v):
    queue = deque()
    queue.append(R)
    visited[R] = 0
    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if visited[i] == -1:
                visited[i] = visited[node] + 1
                queue.append(i)


BFS(R)

for i in visited[1:]:
    print(i)