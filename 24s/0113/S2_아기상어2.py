'''
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
# 그래프이론, 브루트포스, BFS
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

queue = deque()

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            queue.append((i, j))

def BFS():
    while queue:
        x, y = queue.popleft()

        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 0:
                    queue.append((nx, ny))
                    board[nx][ny] = board[x][y] + 1
    return

BFS()

safe = 0
for i in range(N):
    for j in range(M):
        safe = max(safe, board[i][j])

print(safe - 1)