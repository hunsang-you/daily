'''
5
4 3
####
#*@.
####
7 6
###.###
#*#.#*#
#.....#
#.....#
#..@..#
#######
7 4
###.###
#....*#
#@....#
.######
5 5
.....
.***.
.*@*.
.***.
.....
3 3
###
#@#
###

'''
# 그래프 이론, 탐색, BFS
# '.': 빈 공간
# '#': 벽
# '@': 상근이의 시작 위치
# '*': 불
import sys
input = sys.stdin.readline
from collections import deque


T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS():
    cnt = 0

    while me:
        cnt += 1

        while fire and fire[0][2] < cnt:
            x, y, time = fire.popleft()

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < h and 0 <= ny < w:
                    if board[nx][ny] == '.' or board[nx][ny] == '@':
                        board[nx][ny] = '*'
                        fire.append((nx, ny, time + 1))

        while me and me[0][2] < cnt:
            x, y, time = me.popleft()

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < h and 0 <= ny < w:
                    if board[nx][ny] == '.' and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        me.append((nx, ny, time + 1))

                else:
                    return cnt
    return 'IMPOSSIBLE'

for _ in range(T):
    w, h = map(int, input().split())

    board = [list(input().rstrip()) for _ in range(h)]

    fire = deque()
    me = deque()
    visited = [[0] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if board[i][j] == '@':
                visited[i][j] = 1
                me.append((i, j, 0))

            elif board[i][j] == '*':
                fire.append((i, j, 0))


    print(BFS())
