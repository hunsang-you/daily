'''
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
'''
from collections import deque

M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
queue = deque()

# queue에 토마토의 위치를 추가
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            queue.append([i,j])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def BFS():
    while queue:
        x, y = queue.popleft()      # x, y에 추가시켰던 토마토의 위치를 넣는다.

        for i in range(4):      # delta
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:     # 경계조건 : N, M의 크기를 넘지 않고, 익지 않은 토마토가 존재 (0)
                queue.append([nx, ny])                  # 바뀐 위치 추가
                matrix[nx][ny] = matrix[x][y] + 1       # 해당 위치에 1씩 더해주면서 간다

BFS()
answer = 0
# BFS를 다 실행했는데도 matrix에 0이 남아있다면 -1을 출력한다. 아니라면 matrix의 최고값을 구한다.
for i in matrix:
    for j in i :
        if j == 0 :
            print(-1)
            exit(0)
    answer = max(answer, max(i))
print(answer-1)