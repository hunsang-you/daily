'''
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2

'''
# 그래프 이론, 탐색, BFS

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)


def BFS(n):
    queue = deque([n])
    visited[n] = 1

    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = visited[now] + 1
                queue.append(i)

BFS(1)
v = max(visited)
print(visited.index(v), v-1, visited.count(v))