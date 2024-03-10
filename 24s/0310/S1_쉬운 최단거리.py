'''
15 15
2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 1 0 0 0
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
'''
# 그래프이론, 탐색, BFS
#  0은 갈 수 없는 땅이고 1은 갈 수 있는 땅, 2는 목표지점이다

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 0
    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
                if board[nx][ny] == 0:
                    visited[nx][ny] = 0
                elif board[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))


for i in range(N):
    for j in range(M):
        if board[i][j] == 2 and visited[i][j] == -1:
            BFS(i, j)
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=" ")
    print()