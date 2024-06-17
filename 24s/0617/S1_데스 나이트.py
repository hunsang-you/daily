'''
7
6 6 0 1

6
5 1 0 5

7
0 3 4 3
'''
# 그래프 이론, 탐색, BFS
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

r1, c1, r2, c2 = map(int, input().split())
board = [[-1] * N for _ in range(N)]

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    board[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == -1:
                queue.append((nx, ny))
                board[nx][ny] = board[x][y] + 1

BFS(r1, c1)

print(board[r2][c2])