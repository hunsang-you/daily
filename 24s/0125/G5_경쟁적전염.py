'''
3 3
1 0 2
0 0 0
3 0 0
2 3 2

3 3
1 0 2
0 0 0
3 0 0
1 2 2
'''
# BFS

from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
visited = [[0] * N for _ in range(N)]

# 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

virus = []
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            virus.append([board[i][j], i, j, 0])    # virus종류, 좌표, 흐른시간
virus.sort()

queue = deque(virus)

while queue:
    target, r, c, time = queue.popleft()
    if time == S:
        break

    for k in range(4):
        nr = r + dx[k]
        nc = c + dy[k]

        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 0:
            board[nr][nc] = target
            queue.append([target, nr, nc, time+1])

print(board[X-1][Y-1])