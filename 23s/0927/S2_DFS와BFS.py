'''
4 5 1
1 2
1 3
1 4
2 4
3 4

5 5 3
5 4
5 2
1 2
3 4
3 1

1000 1 1000
999 1000
'''
import sys
input = sys.stdin.readline
from collections import deque

N, M, V = map(int,input().split())
graph = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

visited1 = [0] * (N+1)
visited2 = [0] * (N+1)


def dfs(v):
    visited1[v] = 1
    print(v, end=" ")
    for i in range(1, N+1):
        if visited1[i] != 1 and graph[v][i] != 0:
            dfs(i)

def bfs(v):
    visited2[v] = 1
    q = deque([v])
    while q:
        v = q.popleft()
        print(v, end=" ")


        for i in range(1, N+1):
            if visited2[i] != 1 and graph[v][i] != 0:
                q.append(i)
                visited2[i] = 1


dfs(V)
print()
bfs(V)