'''
5 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1

4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

4 10
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1

'''
# DFS

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
visited = [[0] * M for _ in range(N)]

def DFS(n, sum_, tlst):
    global ans

    # 총 4칸이면 return
    if n == 4:
        ans = max(ans, sum_)

        return

    for ci, cj in tlst:     # 도형의 모든위치에서 네방향
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = ci + di
            nj = cj + dj

            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 :
                visited[ni][nj] = 1
                DFS(n+1, sum_ + board[ni][nj], tlst+[(ni, nj)])
                visited[ni][nj] = 0



ans = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        DFS(1, board[i][j], [(i, j)])

print(ans)