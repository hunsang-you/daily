'''
3 4 6
....
.T..
....
'''
# DFS, 그래프이론, 백트래킹

import sys
input = sys.stdin.readline

R, C, K = map(int, input().split())

board = [list(map(str, input().rstrip())) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
answer = 0
def DFS(x, y, dep):
    global answer
    visited[x][y] = 1
    if dep == K and x == 0 and y == C-1:
        answer += 1

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == 0 and board[nx][ny] != 'T':
            visited[nx][ny] = 1
            DFS(nx, ny, dep+1)
            visited[nx][ny] = 0

DFS(R-1, 0, 1)
print(answer)