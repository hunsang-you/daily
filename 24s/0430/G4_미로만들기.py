'''
8
11100110
11010010
10011010
11101100
01000111
00110001
11011000
11000111

'''
# 그래프 이론, 탐색, BFS, 다익스트라, 최단경로, 0-1 우선너비탐색

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

board = [list(input().rstrip()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        if x == N-1 and y == N-1:
            return visited[x][y]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if board[nx][ny] == '1':
                    queue.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
                else:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1


print(BFS(0, 0)-1)