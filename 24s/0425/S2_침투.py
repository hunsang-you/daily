'''
5 6
010101
010000
011101
100011
001011

8 8
11000111
01100000
00011001
11001000
10001001
10111100
01010000
00001011

'''
# 그래프이론, 탐색, BFS, DFS

import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
board = [list(map(str, input().rstrip())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    queue = deque()
    queue.append((int(x), int(y)))

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0:
                if board[nx][ny] == '0':
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
for i in range(N):
    if board[0][i] == '0':
        BFS(0, i)



if 1 in visited[-1]:
    print("YES")
else:
    print("NO")