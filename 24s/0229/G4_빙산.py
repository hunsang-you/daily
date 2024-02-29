'''
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0

'''
# 그래프이론,탐색, BFS, DFS
# pypy
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def BFS(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if board[nx][ny] != 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

                else:
                    cnt[x][y] += 1
    return 1



time = 0
while True:
    visited = [[0] * M for _ in range(N)]
    cnt = [[0] * M for _ in range(N)]
    block = []

    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 and visited[i][j] == 0:
                block.append(BFS(i, j))

    for i in range(N):
        for j in range(M):
            board[i][j] -= cnt[i][j]
            if board[i][j] < 0:
                board[i][j] = 0

    if len(block) == 0 or len(block) >= 2:
        break

    time += 1

if len(block) >= 2:
    print(time)

else:
    print(0)