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
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            queue.append([i,j])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def BFS():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:
                queue.append([nx, ny])
                matrix[nx][ny] = matrix[x][y] + 1

BFS()
answer = 0
for i in range(N):
    for j in range(M) :
        if matrix[i][j] == 0 :
            print(-1)

        else:
            if answer < matrix[i][j] :
                answer = matrix[i][j]
print(answer - 1)


# for i in range(N):
#     for j in range(M) :
#         # BFS를 다 실행했는데도 matrix에 0이 남아있다면 -1을 출력한다. 아니라면 matrix의 최고값을 구한다.
#         if matrix[i][j] == 0 :
#             print(-1)
#             exit(0)
#         else:
#             if answer < matrix[i][j]:
#                 answer = matrix[i][j]
#
# print(answer - 1)