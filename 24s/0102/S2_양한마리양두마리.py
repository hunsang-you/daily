'''
2
4 4
#.#.
.#.#
#.##
.#.#
3 5
###.#
..#..
#.###
'''
# DFS
import sys
sys.setrecursionlimit(10**6)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

T = int(input())

def DFS(y, x):
    board[y][x] = '.'
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < W and 0 <= ny < H:
            if board[ny][nx] == '#':
                DFS(ny, nx)


for tc in range(T):
    H, W = map(int, input().split())
    board = [list(input()) for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if board[i][j] == '#':
                DFS(i, j)
                cnt += 1

    print(cnt)