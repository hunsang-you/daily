'''
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
'''
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def func(x, y, h):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
            if board[nx][nx] > h:
                visited[nx][ny] = 1
                func(nx, ny, h)


N = int(input())
board = []
highest = 0
ans = 1
for i in range(N):
    line = list(map(int, input().split()))
    board.append(line)
    for j in line:
        if j > highest :
            highest = j

for k in range(highest):
    visited = [[0] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] > k and visited[i][j] == 0:
                cnt += 1
                visited[i][j] = 1
                func(i, j, k)

    ans = max(ans, cnt)


print(ans)