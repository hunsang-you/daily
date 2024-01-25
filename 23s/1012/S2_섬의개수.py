'''
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
'''
# DFS, BFS
# 한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다.
#
# 두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.
# 1 = 땅 0 = 바다
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
def DFS(x, y):
    # 상하좌우대각(시계방향)
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    board[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != 0:
            DFS(nx, ny)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0 :
        break

    board = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                DFS(i, j)
                cnt += 1
    print(cnt)