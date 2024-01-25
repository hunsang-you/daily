'''
5 3 1
0 -1 0 0 0
-1 -1 0 1 1
0 0 0 1 1
5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
'''
from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
matrix = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
queue = deque()

# queue에 토마토의 위치를 추가
for i in range(H):
    for j in range(N):
        for k in range(M):
            if matrix[i][j][k] == 1:
                queue.append([i,j,k])

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def BFS():
    while queue:
        z, x, y = queue.popleft()      # x, y에 추가시켰던 토마토의 위치를 넣는다.

        for i in range(6):      # delta
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if -1 < nx < N and -1 < ny < M and -1 < nz < H:
                if matrix[nz][nx][ny] == 0 :
                    matrix[nz][nx][ny] = matrix[z][x][y] + 1
                    queue.append((nz, nx, ny))

BFS()
check = 0
answer = -2
# BFS를 다 실행했는데도 matrix에 0이 남아있다면 -1을 출력한다. 아니라면 matrix의 최고값을 구한다.
for i in range(H):
    for j in range(N) :
        for k in range(M):
            if matrix[i][j][k] == 0 :
                check = 1

            answer = max(answer, matrix[i][j][k])

if check == 1:
    print(-1)
elif answer == -1:
    print(0)
else:
    print(answer-1)