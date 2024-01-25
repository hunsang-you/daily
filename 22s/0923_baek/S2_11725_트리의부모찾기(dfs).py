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
sys.setrecursionlimit(1000000)

def dfs(s):
    for i in graph[s]:
        if visited[i] == 0:
            visited[i] = s
            dfs(i)

N = int(input())
V = N - 1
graph = [[] for _ in range(N+1)]
for _ in range(V):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N+1)

arr = []
dfs(1)

for i in range(2, N+1):
    print(visited[i])
