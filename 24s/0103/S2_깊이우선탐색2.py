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

def DFS(r):
    global cnt
    visited[r] = True
    answer[r] = cnt
    graph[r].sort(reverse=True)

    for i in graph[r]:
        if not visited[i]:
            cnt += 1
            DFS(i)


N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
answer = [0] * (N+1)
cnt = 1
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

DFS(R)

for i in answer[1:]:
    print(i)