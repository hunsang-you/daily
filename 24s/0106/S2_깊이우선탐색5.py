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

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [-1] * (N+1)
depth = 0
cnt = 0
result = 0
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N+1):
    graph[i].sort()

def DFS(depth, r):
    global cnt, result
    cnt += 1
    visited[r] = depth * cnt
    result += visited[r]

    for i in graph[r]:
        if visited[i] == -1:
            DFS(depth+1, i)

DFS(depth,R)

print(result)
