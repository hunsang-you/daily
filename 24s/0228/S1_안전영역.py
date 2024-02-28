'''
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7

7
9 9 9 9 9 9 9
9 2 1 2 1 2 9
9 1 8 7 8 1 9
9 2 7 9 7 2 9
9 1 8 7 8 1 9
9 2 1 2 1 2 9
9 9 9 9 9 9 9

'''
# BFS, DFS

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = []
rain = 0

for i in range(N):
    board.append(list(map(int, input().split())))
    for j in range(N):
        if board[i][j] > rain:
            rain = board[i][j]


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def BFS(x, y, rain, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N :
                if visited[nx][ny] == 0 and board[nx][ny] > rain:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

answer = 0
for k in range(rain):
    visited = [[0] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] > k and visited[i][j] == 0:
                BFS(i, j, k, visited)
                cnt += 1

    if answer < cnt:
        answer = cnt

print(answer)

