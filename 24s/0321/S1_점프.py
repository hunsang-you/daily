'''
4
2 3 3 1
1 2 1 3
1 2 3 1
3 1 1 0

'''
# 다이나믹 프로그래밍

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

DP = [[0] * N  for _ in range(N)]
DP[0][0] = 1
for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            print(DP[i][j])


        # 오른쪽으로 이동하는 경우
        if j + board[i][j] < N:     # N의 범위 내에서만
            DP[i][j + board[i][j]] += DP[i][j]

        if i + board[i][j] < N:
            DP[i + board[i][j]][j] += DP[i][j]

