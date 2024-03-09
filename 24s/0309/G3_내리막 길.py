'''
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
'''
# 다이나믹 프로그래밍, 그래프이론,탐색, DFS

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
ans = 0
def DFS(x, y):
    global ans
    if x == N-1 and y == M-1:
        return 1

    if visited[x][y] != -1:
        return visited[x][y]

    visited[x][y] = 0


    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < N and 0 <= ny < M :
            if board[x][y] > board[nx][ny]:
                visited[x][y] += DFS(nx, ny)
    return visited[x][y]

print(DFS(0, 0))