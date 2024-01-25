'''
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW
'''
# readline()을 사용해도 시간초과가 뜬다.
# pypy로 제출
# import time
# start = time.time()

import sys
from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

cnt = 0


def bfs(x, y):
    global cnt
    queue = deque()
    queue.append((x, y))        # 시작점 저장

    while queue:        # 큐가 빌때까지
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and board[nx][ny] == 'L':
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                cnt = max(visited[nx][ny], cnt)     # 이전의 최대값과 비교하여 더 큰 값으로 대체
            # for v in visited:
            #     print(*v)
            # print('#=====')
    return cnt

# (0,0)부터 (N, M)까지 탐색
for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':      # 시작지점이 육지라면 탐색 시작
            visited = [[0] * M for _ in range(N)]      # 새로 탐색할 때마다 visited 초기화
            visited[i][j] = 1   # 탐색 시작점을 0으로
            bfs(i, j)

print(cnt-1)

# print("time :", time.time() - start)            # 약 1.21초