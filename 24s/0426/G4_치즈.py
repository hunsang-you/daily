'''
13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0

'''
# 구현, 그래프이론, 탐색, 시뮬레이션, BFS

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0
cheeze = []
def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 0 and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

                elif board[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1

while True:
    visited = [[0] * M for _ in range(N)]

    BFS(0, 0)
    ans += 1
    cnt = 0
    air_cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 2:
                board[i][j] = 0
                cnt += 1
            if board[i][j] == 0:
                air_cnt += 1


    cheeze.append(cnt)

    if air_cnt == N * M:
        break

print(ans)
print(cheeze[-1])