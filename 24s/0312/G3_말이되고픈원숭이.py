'''
1
4 4
0 0 0 0
1 0 0 0
0 0 1 0
0 1 0 0

2
5 2
0 0 1 1 0
0 0 1 1 0

'''
# 그래프이론, 탐색, BFS

import sys
input = sys.stdin.readline
from collections import deque

K = int(input())

W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

hor_x = [1, 2, 1, 2, -1, -2, -1, -2]
hor_y = [2, 1, -2, -1, 2, 1, -2, -1]

def BFS(x, y, K):
    queue = deque()
    queue.append((x, y, K))
    visited = [[[0] * (K+1) for _ in range(W)] for _ in range(H)]
    visited[x][y][0] = 1



    while queue:
        x, y, K = queue.popleft()

        if x == H-1 and y == W-1:
            return visited[x][y][K]

        if K > 0:
            for k in range(8):
                nx = x + hor_x[k]
                ny = y + hor_y[k]

                if 0 <= nx < H and 0 <= ny < W:
                    if board[nx][ny] != 1 and visited[nx][ny][K-1] == 0:
                        visited[nx][ny][K-1] = visited[x][y][K] + 1
                        queue.append((nx, ny, K-1))

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < H and 0 <= ny < W:
                if visited[nx][ny][K] == 0 and board[nx][ny] == 0:
                    visited[nx][ny][K] = visited[x][y][K] + 1
                    queue.append((nx, ny, K))


    return -1

print(BFS(0, 0, K))