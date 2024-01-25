'''
5 5 1
1 4
1 2
2 3
2 4
3 4
'''
# DFS

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**8)

def DFS(v, dep):
    visited[v] = dep

    for i in graph[v]:
        if visited[i] == -1:
            DFS(i, dep+1)


N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [-1 for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort(reverse=True)

DFS(R, 0)
for i in range(1, N+1):
    print(visited[i])