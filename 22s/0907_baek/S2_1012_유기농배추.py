'''
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
'''
import sys
sys.setrecursionlimit(10**6)
T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())

    farm = [[0] * M for _ in range(N)]      # 배추가 심어진 농장
    visited = [[0] * M for _ in range(N)]       # 개미가 방문한곳

    cnt = 0
    # 배추가 있는 곳을 표시
    for _ in range(K):
        y, x = map(int, input().split())
        farm[x][y] = 1

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    def DFS(x, y):
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M :
                if farm[nx][ny] == 1:
                    if visited[nx][ny] == 0 :
                        DFS(nx, ny)



    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1:
                if visited[i][j] == 0:
                    DFS(i, j)
                    cnt += 1


    print(cnt)










