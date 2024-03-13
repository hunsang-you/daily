'''
4 4
####
#JF#
#..#
#..#

'''
# 그래프이론, 탐색, BFS

import sys
input = sys.stdin.readline
from collections import deque


R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
queue = deque()


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def BFS(queue):

    while queue:
        x, y, s = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < R and 0 <= ny < C:
                if not visited[nx][ny] and board[nx][ny] == '.':
                    queue.append((nx, ny, s))
                    visited[nx][ny] = visited[x][y] + 1
            else:
                if s == 'J':
                    return visited[x][y]



for i in range(R):
    for j in range(C):
        if board[i][j] == 'J':
            visited[i][j] = 1
            queue.append((i, j, 'J'))
        if board[i][j] == 'F':
            visited[i][j] = 1
            queue.appendleft((i, j, 'F'))

ans = BFS(queue)

if ans:
    print(ans)
else:
    print('IMPOSSIBLE')