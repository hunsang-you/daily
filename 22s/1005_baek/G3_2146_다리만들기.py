import sys; sys.stdin = open('다리')
'''
10
1 1 1 0 0 0 0 1 1 1
1 1 1 1 0 0 0 0 1 1
1 0 1 1 0 0 0 0 1 1
0 0 1 1 1 0 0 0 0 1
0 0 0 1 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0
'''
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def BFS(i, j):
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
            if board[nx][ny] == 1 : continue
            visited[nx][ny] = visited[i][j] + 1
            BFS(nx, ny)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 :
            visited[i][j] = 1
            BFS(i, j)

for i in visited:
    print(*i)