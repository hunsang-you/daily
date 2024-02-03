'''
5 5
WBWWW
WWWWW
BBBBB
BBBWW
WWWWW
'''
# DFS BFS

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(input().rstrip()) for _ in range(M)]

blue, white = 0, 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(i, j, color, cnt):
    board[i][j] = 0

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < M and 0 <= ny < N  and color == board[nx][ny]:
            cnt = DFS(nx, ny, color, cnt+1)
    return cnt



for i in range(M):
    for j in range(N):
        if board[i][j] == 'W':
            white += DFS(i, j, 'W', 1) ** 2


        elif board[i][j] == 'B':
            blue += DFS(i, j, 'B', 1) ** 2


print(white, blue)