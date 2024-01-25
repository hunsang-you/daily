'''
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2
'''
from collections import deque

def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and board[nx][ny] == 0:
                board[nx][ny] = 1
                queue.append((nx, ny))
                cnt += 1
    return cnt


M, N, K = map(int, input().split())
board = [[0] * N for _ in range(M)]


# 주어진 영역에 대해 +1
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] += 1

# board[i][j] == 0 에서 BFS를 실행
result = []
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            board[i][j] += 1
            result.append(BFS(i, j))

result.sort()

print(len(result))
print(*result)