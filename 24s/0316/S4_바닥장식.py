'''
4 4
----
----
----
----

6 9
-||--||--
--||--||-
|--||--||
||--||--|
-||--||--
--||--||-

7 8
--------
|------|
||----||
|||--|||
||----||
|------|
--------

10 10
||-||-|||-
||--||||||
-|-|||||||
-|-||-||-|
||--|-||||
||||||-||-
|-||||||||
||||||||||
||---|--||
-||-||||||

6 6
-||--|
||||||
|||-|-
-||||-
||||-|
||-||-

'''
# 구현, 그래프 이론, 탐색, BFS

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(input().rstrip()) for _ in range(N)]

def DFS(x, y):
    if board[x][y] == '-':
        board[x][y] = 1

        for dy in [-1, 1]:
            ny = y + dy

            if 0 <= ny < M and board[x][ny] == '-':
                DFS(x, ny)

    if board[x][y] == '|':
        board[x][y] = 1

        for dx in [-1, 1]:
            nx = x + dx

            if 0 <= nx < N and board[nx][y] == '|':
                DFS(nx, y)


ans = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == '-' or board[i][j] == '|':
            DFS(i, j)
            ans += 1

print(ans)