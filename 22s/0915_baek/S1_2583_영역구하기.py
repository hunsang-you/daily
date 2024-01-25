'''
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2
'''
from collections import deque

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    cnt = 1
    while queue:
        y, x = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and board[ny][nx] == 0:
                board[ny][nx] = 1
                queue.append((ny, nx))
                cnt += 1
    return cnt



M, N, K = map(int, input().split())     # M : 세로    N : 가로   K : 직사각형의 개수
board = [[0] * N for _ in range(M)]
result = []


# 직사각형이 포함된 board영역은 1을 더해준다.
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] += 1

# board[i][j] == 0 인 지점에 대해 bfs를 실행한다
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            board[i][j] += 1
            result.append(bfs(i, j))


result.sort()

print(len(result))
print(*result)