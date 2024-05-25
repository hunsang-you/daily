'''
3 2

4 5

1000 1000

'''
# 구현, 문자열

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

DP = [[0] * (M+1) for _ in range(N+1)]

DP[0][0] = 1

for i in range(1, N+1):
    for j in range(1, M+1):
        DP[i][j] = (DP[i-1][j] + DP[i][j-1] + DP[i-1][j-1]) % 1000000007

print(DP[N][M])