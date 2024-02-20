'''
2 20 50
50 30
20 40

2 40 50
50 30
20 40

2 20 50
50 30
30 40

3 5 10
10 15 20
20 30 25
40 22 10

4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10
'''
# 그래프이론, DFS, 시뮬레이션

import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

answer = 0
queue = deque()

def BFS(a, b):
    queue.append((a, b))
    union = []
    union.append((a, b))
    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx >= N or nx < 0 or ny >= N or ny < 0 or visited[nx][ny] == 1:
                continue
            if (L <= abs(board[nx][ny] - board[x][y]) <= R):

                visited[nx][ny] = 1
                queue.append((nx, ny))
                union.append((nx, ny))

    if len(union) <= 1:
        return 0

    temp = sum(board[x][y] for x, y in union) // len(union)

    for x, y in union:
        board[x][y] = temp
    return 1

while True:
    check = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                check += BFS(i, j)

    if check == 0:
        break

    answer += 1

print(answer)