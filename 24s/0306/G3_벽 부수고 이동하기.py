'''
6 4
0100
1110
1000
0000
0111
0000

4 4
0111
1111
1111
1110

'''
# 그래프 이론, 탐색, BFS

import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int, input().split())

board = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]   # 방문 여부 및 부술수 있는지에 대해 3차원으로 확인
# visited[x][y][0] = 0 (안부숨) visited[x][y][1] = 1 (부숨)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited[0][0][0] = 1
def BFS(x, y, z):
    global ans
    queue = deque()
    queue.append((x, y, z))

    while queue:
        x, y, z = queue.popleft()

        if x == N-1 and y == M-1:
            return visited[x][y][z]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M :
                # 벽을 한번 부수고 가는 경우
                if board[nx][ny] == 1 and z == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))


                # 벽이 없는 곳만 가는 경로
                elif board[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append((nx, ny, z))

    # 불가능하면 -1
    return -1


print(BFS(0, 0, 0))
