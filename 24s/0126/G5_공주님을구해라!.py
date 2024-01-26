'''
6 6 16
0 0 0 0 1 1
0 0 0 0 0 2
1 1 1 0 1 0
0 0 0 0 0 0
0 1 1 1 1 1
0 0 0 0 0 0

3 4 100
0 0 0 0
1 1 1 1
0 0 2 0
'''
# BFS

import sys
input = sys.stdin.readline
from collections import deque

N, M, T = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append((0, 0, 0))
visited[0][0] = True
result = 1e9
while queue:
    x, y, t = queue.popleft()

    if x == N-1 and y == M-1:
        result = min(result, t)
        break

    if t + 1 > T:
        break

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False:
            if board[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny, t+1))
            elif board[nx][ny] == 1:
                continue

            elif board[nx][ny] == 2:
                temp = t + 1
                temp += abs(N-1-nx) + abs(M-1-ny)
                visited[nx][ny] = True
                if temp <= T:
                    result = temp

if result > T:
    print('Fail')
else:
    print(result)