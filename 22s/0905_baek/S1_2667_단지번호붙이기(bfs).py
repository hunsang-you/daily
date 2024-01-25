'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''
from collections import deque

N = int(input())
board = [list(map(int, input())) for _ in range(N)]
num = []
def BFS(x, y):
    global cnt
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    queue = deque()
    queue.append((x, y))
    board[x][y] = 0         # 탐색중인 위치를 0으로 바꿔 다시 방문하지 않게 한다
    cnt = 1

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >=N or ny < 0 or ny >= N:
                continue

            if board[nx][ny] == 1:      # 만약 방문한 곳이 1이라면 0으로 바꾼다.
                board[nx][ny] = 0
                queue.append((nx, ny))      # 큐에 방문했었던 nx, ny를 넣고 반복
                cnt += 1
    return cnt

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            num.append(BFS(i, j))

num.sort()

print(len(num))

for i in range(len(num)):
    print(num[i])
