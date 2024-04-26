'''
8 9
0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0
0 0 0 1 1 0 1 1 0
0 0 1 1 1 1 1 1 0
0 0 1 1 1 1 1 0 0
0 0 1 1 0 1 1 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

'''
# 구현, 그래프이론, 탐색, 시뮬레이션, BFS, DFS

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
# 공기를 위주로 돌도록
def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M :
                if board[nx][ny] == 0 and visited[nx][ny] == 0:     # 이동한 곳이 공기면 추가
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

                elif board[nx][ny] == 1:        # 이동한 곳이 치즈라면 방문횟수만큼 더 증가
                    visited[nx][ny] = visited[nx][ny] + 1



while True:
    visited = [[0] * M for _ in range(N)]       # 한차례 돌고나면 초기화도 되도록

    # 한번 돌면 시간 + 1
    BFS(0, 0)
    ans += 1
    air_cnt = 0             # 공기칸의 개수
    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 2:      # 두번이상 방문했다면 공기에 2번이상 노출된것이므로 치즈소멸
                board[i][j] = 0

            if board[i][j] == 0:
                air_cnt += 1

    if air_cnt == N * M:
        break
print(ans)



