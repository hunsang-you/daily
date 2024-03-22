'''
remind
5 4
0 0 1 0
0 0 0 0
1 0 0 0
0 0 0 0
0 0 0 1

7 4
0 0 0 1
0 1 0 0
0 0 0 0
0 0 0 1
0 0 0 0
0 1 0 0
0 0 0 1

'''
# 그래프 이론, 탐색, 브루트포스, BFS

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


queue = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            queue.append((i, j))

def BFS(queue):
    while queue:
        x, y = queue.popleft()

        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M :
                if board[nx][ny] == 0:
                    queue.append((nx, ny))
                    board[nx][ny] = board[x][y] + 1

    return 1

BFS(queue)

zone = 0

for i in range(N):
    for j in range(M):
        zone = max(zone, board[i][j])

print(zone-1)