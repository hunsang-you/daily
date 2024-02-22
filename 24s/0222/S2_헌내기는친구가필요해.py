'''
3 5
OOOPO
OIOOX
OOOXP

3 3
IOX
OXP
XPP
'''
# 그래프이론,탐색, DFS, BFS
# O는 빈 공간, X는 벽, I는 도연이, P는 사람이다. I가 한 번만 주어짐이 보장된다
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

campus = [list(input().rstrip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

queue = deque()

answer = 0
def BFS():
    global answer
    for i in range(N):
        for j in range(M):
            if campus[i][j] == 'I':
                queue.append((i, j))
                visited[i][j] = 1

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and campus[nx][ny] != 'X' and visited[nx][ny] == 0:

                if campus[nx][ny] == 'O':
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

                elif campus[nx][ny] == 'P':
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    answer += 1


BFS()
if answer == 0:
    print('TT')
else:
    print(answer)