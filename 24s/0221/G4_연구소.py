'''
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
'''
# 그래프 이론, BFS, 브루트포스

import sys
import copy
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
answer = 0
def BFS(x, y):
    global answer
    queue.append((x, y))
    visited = [[0] * M for _ in range(N)]
    new_board = copy.deepcopy(board)
    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and new_board[nx][ny] == 0:
                visited[nx][ny] = 1
                new_board[nx][ny] = 2
                queue.append((nx, ny))

    cnt = 0

    for i in range(N):
        cnt += new_board[1].count(0)
    answer = max(answer, cnt)



def wall(cnt):
    if cnt == 3:
        for i in range(N):
            for j in range(M):
                BFS(i, j)
                return

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                wall(cnt+1)
                board[i][j] = 0

wall(0)
print(answer)
