'''
3
0 0 0
0 0 0
0 9 0

3
0 0 1
0 0 0
0 9 0

4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4

6
5 4 3 2 3 4
4 3 2 3 4 5
3 2 9 5 6 6
2 1 2 3 4 5
3 2 1 6 5 4
6 6 6 6 6 6

6
6 0 6 0 6 1
0 0 0 0 0 2
2 3 4 5 6 6
0 0 0 0 0 2
0 2 0 0 0 0
3 9 3 0 0 1

6
1 1 1 1 1 1
2 2 6 2 2 3
2 2 5 2 2 3
2 2 2 4 6 3
0 0 0 0 0 6
0 0 0 0 0 9

'''
# 구현, 그래프 이론, 탐색, 시뮬레이션, BFS


import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
shark_size = 2

queue = deque()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def BFS(x, y):
    global shark_size
    queue.append((x, y, 0))

    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    while queue:
        x, y, time = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N:
                # 그냥 이동시
                if visited[nx][ny] == 0 and board[nx][ny] == 0:
                    queue.append((nx, ny, time + 1))
                    visited[nx][ny] = visited[x][y] + 1
                # 물고기를 먹을수 있을 때
                if visited[nx][ny] == 0 and board[nx][ny] != 0 and board[nx][ny] < shark_size:
                    if shark_size == board[nx][ny] :
                        shark_size += 1
                    board[nx][ny] = 0
                    queue.append((nx, ny, time + 1))
                    visited[nx][ny] = visited[x][y] + 1

    return visited

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            print(BFS(i, j))
