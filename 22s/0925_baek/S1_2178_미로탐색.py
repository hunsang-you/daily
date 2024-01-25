'''
4 6
101111
101010
101011
111011
4 6
110110
110110
111111
111101
'''
from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def BFS(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1:
                queue.append((nx, ny))
                board[nx][ny] = board[x][y] + 1
    return board[N-1][M-1]



N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]

print(BFS(0,0))
