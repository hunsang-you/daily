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


def BFS(x, y):
    queue = deque()
    visited = [[0] * w for _ in range(h)]
    queue.append((x, y))
    visited[x][y] = 1

    # 불이 위치한 곳을 -1로 방문표시
    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                visited[i][j] = -1
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 > nx or h < nx or 0 > ny or w < ny:
                return visited[x][y]

            elif 0 <= nx < h and 0 <= ny < w:
                if board[nx][ny] == '.':
                    if visited[x][y] > 0 and visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))

                    elif visited[nx][ny] >= 0 and visited[x][y] == -1:
                        visited[nx][ny] = -1
                        queue.append((nx, ny))
    return 'IMPOSSIBLE'

for _ in range(T):
    w, h = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if board[i][j] == '@':
                print(BFS(i, j))
                break