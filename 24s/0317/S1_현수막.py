'''
8 19
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 0
0 0 1 0 1 0 0 1 1 0 0 1 0 0 0 1 0 0 0
0 1 0 0 0 1 0 1 0 1 0 1 0 0 0 1 0 0 0
0 1 1 1 1 1 0 1 0 1 0 1 0 0 0 1 0 0 0
0 1 0 0 0 1 0 1 0 0 1 1 0 0 0 1 0 0 0
0 1 0 0 0 1 0 1 0 0 0 1 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

'''
# 그래프 이론, 탐색, BFS, DFS

import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]


def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < M and 0 <= ny < N:
                if visited[nx][ny] == 0 and board[nx][ny] == 1:
                        queue.append((nx, ny))
                        board[nx][ny] = 0



    return 1

ans = 0
for i in range(M):
    for j in range(N):
        if board[i][j] == 1:
            ans += BFS(i, j)

print(ans)
