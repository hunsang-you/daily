'''
6 5
1 2
2 5
5 1
3 4
4 6
'''
import sys
sys.setrecursionlimit(1000000)
def DFS(v):
    visited[v] = 1
    for i in graph[v]:              # v요소에 대해 방문하지 않았으면 1로 바꾸고 재귀
        if visited[i] == 0:
            visited[i] = 1
            # print(visited)
            DFS(i)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):          # 그래프 그리기
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0

for i in range(1, N+1):
    if visited[i] == 0:     # 방문하지 않은 곳이면 cnt +1 해주고 DFS돌리기
        cnt += 1
        DFS(i)


print(cnt)