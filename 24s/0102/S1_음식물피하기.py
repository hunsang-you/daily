'''
3 4 5
3 2
2 2
3 1
2 3
1 1
'''

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [[0] * (M+1) for _ in range(N+1)]

for i in range(K):
    r, c = map(int, input().split())
    board[r][c] = 1

visited = [[0] * (M+1) for _ in range(N+1)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
answer = 0
def DFS(x, y):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 < nx <= N and 0 < ny <= M:
            if board[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                cnt += 1
                DFS(nx, ny)

for i in range(N+1):
    for j in range(M+1):
        if board[i][j] == 1 and visited[i][j] == 0:
            cnt = 0
            DFS(i, j)
            answer = max(answer, cnt)
print(answer)