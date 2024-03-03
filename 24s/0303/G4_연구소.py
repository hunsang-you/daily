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

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
answer = 0
def BFS():
    global answer
    queue = deque()
    new_board = copy.deepcopy(board)
    for i in range(N):
        for j in range(M):
            if new_board[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 > nx or N <= nx or 0 > ny or M <= ny:
                continue
            if new_board[nx][ny] == 0:
                new_board[nx][ny] = 2
                queue.append((nx, ny))

    cnt = 0

    for i in range(N):
        cnt += new_board[i].count(0)
    answer = max(answer, cnt)



def wall(cnt):
    if cnt == 3:
        BFS()
        return

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                wall(cnt+1)
                board[i][j] = 0

wall(0)
print(answer)
