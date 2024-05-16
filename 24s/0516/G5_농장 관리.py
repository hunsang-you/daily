'''
8 7
4 3 2 2 1 0 1
3 3 3 2 1 0 1
2 2 2 2 1 0 0
2 1 1 1 1 0 0
1 1 0 0 0 1 0
0 0 0 1 1 1 0
0 1 2 2 1 1 0
0 1 1 1 2 1 0

'''
# 그래프이론, 탐색, BFS, DFS

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

checkidx = []
def DFS(i, j, checkidx):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1
    check = [(i, j)]
    while queue:
        x, y = queue.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and board[nx][ny] != 0:
                    if board[nx][ny] > board[x][y]:
                        return 0
                    if board[x][y] == board[nx][ny]:
                        visited[nx][ny] = 1
                        queue.append((nx, ny))
                        check.append((nx, ny))
        checkidx += check
    return 1

ans = 0
for i in range(N):
    for j in range(M):
        if (i, j) not in checkidx:
            visited = [[0] * M for _ in range(N)]
            ans += DFS(i, j, checkidx)

print(ans)