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
# 그래프이론, 브루트 포스, 그래프 탐색, 너비 우선 탐색
# 연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.
# 일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

import sys
import copy
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
result = 0

def wall(count):
    if count == 3:
        BFS()
        return
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0 :
                board[i][j] = 1
                wall(count+1)
                board[i][j] = 0

def BFS():
    global result
    queue = deque()
    temp = copy.deepcopy(board)
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + d[k][0]
            ny = y + d[k][1]

            if (0 <= nx <N) and (0 <= ny < M):
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    queue.append((nx, ny))

    count = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                count += 1
    result = max(result, count)

wall(0)
print(result)