'''
10
1 1 1 0 0 0 0 1 1 1
1 1 1 1 0 0 0 0 1 1
1 0 1 1 0 0 0 0 1 1
0 0 1 1 1 0 0 0 0 1
0 0 0 1 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0

'''
# 그래프 이론, 탐색, 너비우선탐색

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 섬 찾기
def BFS(i, j):
    queue = deque()
    queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and board[nx][ny] == 1:
                visited[nx][ny] = 1
                queue.append((i, j))
                board[nx][ny] = area


# 섬에서 섬까지 최단거리 찾기
def BFS2(island):
    queue = deque()
    distance = [[-1] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] == island:
                queue.append((i, j))
                distance[i][j] = 0
    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N:
                # 다른 섬만남
                if board[nx][ny] != island and board[nx][ny] != 0:
                    return distance[nx][ny]
                # 물이고 아직 안 지남
                elif board[nx][ny] == 0 and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
    return int(1e9)

area = 1
for i in range(N):
    for j in range(N):
        if board[i][j] and visited[i][j] == 0:
            visited[i][j] = 1
            board[i][j] = area
            BFS(i, j)
            area += 1


result = int(1e9)
for island in range(1, area):
    result = min(result, BFS2(island))

print(result)