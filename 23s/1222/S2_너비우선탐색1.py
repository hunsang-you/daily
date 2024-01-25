'''
5 5 1
1 4
1 2
2 3
2 4
3 4
'''
# BFS

from collections import deque
import sys
input = sys.stdin.readline


def BFS(v):
    global cnt

    queue = deque([R])
    visited[R] = 1

    while queue:
        v = queue.popleft()
        graph[v].sort()
        for i in graph[v]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                queue.append(i)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

BFS(R)

for i in visited[1:]:
    print(i)