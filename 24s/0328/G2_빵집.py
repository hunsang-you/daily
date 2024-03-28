'''
5 5
.xx..
..x..
.....
...x.
...x.

6 10
..x.......
.....x....
.x....x...
...x...xx.
..........
....x.....

'''
# 그래프이론,탐색, 그리디 알고리즘, DFS

import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(map(str, input().rstrip())) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
cnt = 0
# 오른쪽위, 오른쪽, 오른쪽아래
dx = [-1, 0, 1]
dy = [1, 1, 1]

def DFS(x, y):
    global cnt
    visited[x][y] = 1
    if y == C-1:
        cnt += 1
        return True
    for k in range(3):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < R and 0 <= ny < C:
            if board[nx][ny] != 'x' and visited[nx][ny] == 0:
                if DFS(nx, ny):
                    return True


for i in range(R):
    DFS(i, 0)

print(cnt)
