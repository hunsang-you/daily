'''
3 3
D.*
...
.S.

3 3
D.*
...
..S

3 6
D...*.
.X.X..
....S.

5 4
.D.*
....
..X.
S.*.
....

'''
# 그래프 이론, 탐색, BFS

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

# . : 빈곳, * : 물, X : 돌, D : 비버의 굴, S : 고슴도치 위치
board = [list(input().rstrip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
Dx, Dy = 0, 0
queue = deque()

def BFS(i, j):
    while queue:
        x, y = queue.popleft()

        if board[i][j] == 'S':
            return visited[i][j]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                if (board[nx][ny] == '.' or board[nx][ny] == 'D') and board[x][y] == 'S':
                    board[nx][ny] = 'S'
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

                elif (board[nx][ny] == '.' or board[nx][ny] == 'S') and board[x][y] == '*':
                    board[nx][ny] = '*'
                    queue.append((nx, ny))
    return 'KAKTUS'


for x in range(N):
    for y in range(M):
        if board[x][y] == 'S':
            queue.append((x,y))
        elif board[x][y] == 'D':
            Dx,Dy = x,y

for x in range(N):
    for y in range(M):
        if board[x][y] == '*':
            queue.append((x,y))

print(BFS(Dx,Dy))