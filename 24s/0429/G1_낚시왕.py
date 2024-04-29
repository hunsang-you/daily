'''
5 4
0 0 1 0 2
2 3 2 1 0
4 3 2 9 0
1 0 2 9 0
8 8 2 1 0
1 3
3 4
8 1
4 8

5 8
0 0 1 0 2
2 3 2 1 0
0 0 2 0 0
1 0 2 0 0
0 0 2 1 0
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2

5 8
100 100 100 100 100
100 100 100 100 100
100 100 100 100 100
100 100 100 100 100
100 100 100 100 100
8 1
7 1
6 1
5 1
4 1
3 1
2 1
1 1

'''
# 구현, 시뮬레이션

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cloud_1 = [[N-2, 0], [N-2, 1], [N-1, 0], [N-1, 1]]      # 구름 초기위치
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
ans = 0

for _ in range(M):
    d, s = map(int, input().split())
    # [1] 구름 이동 [2] 물 증가 [3] 구름 사라짐(cloud_2에 좌표저장)
    cloud_2 = []            # 이동할 구름 위치 저장
    for x, y in cloud_1:
        nx, ny = (x + dx[d] * s + N) % N, (y + dy[d] * s + N) % N       # 양쪽끝이 연결되어 있으므로
        board[nx][ny] += 1          # 물증가
        cloud_2.append((nx, ny))


    # 구름이 이동한 위치에서 대각선 확인
    v = [[0] * N for _ in range(N)]
    for x, y in cloud_2:
        v[x][y] = 1
        for di, dj in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
            nx, ny = x + di, y + dj
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] > 0:
                board[x][y] += 1

    # 전체 순회 물 >= 2 인 자리는 구름발생하고 -2, 단 cloud_2 위치 제외
    cloud_1 = []
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and v[i][j] == 0:

                board[i][j] -= 2
                cloud_1.append((i, j))
for lst in board:

    ans += sum(lst)

print(ans)