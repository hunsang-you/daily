'''
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
'''
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def BFS(x, y):
    cnt = 1
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 1 and visited[nx][ny] == 0 :
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    cnt += 1
    return cnt


N, M = map(int, input().split())
visited = [[0] * M for _ in range(N)]
board = [list(map(int, input().split())) for _ in range(N)]

total, cnt = 0, 0

for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and visited[i][j] == 0:
            total += 1
            cnt = max(cnt, BFS(i, j))

print(total)
print(cnt)